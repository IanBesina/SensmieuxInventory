from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.db.models import Sum
from more_itertools import quantify
from re import I

# Create your models here.

class Product(models.Model):
    code=models.CharField(max_length=100,blank=True, null=True)
    name=models.CharField(max_length=250,blank=True, null=True)
    lotnumber = models.TextField(max_length=250,blank=True, null=True)
    cost = models.FloatField(default=0)
    price = models.FloatField(default=0)
    expiry = models.TextField(max_length=250,blank=True, null=True)
    status = models.CharField(max_length=2, choices=(('1','Active'),('2','Inactive')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code + ' - ' + self.name

    def count_inventory(self):
        stocks = Stock.objects.filter(product = self)
        stockIn = 0
        stockOut = 0
        for stock in stocks:
            if stock.type == '1':
                stockIn = int(stockIn) + int(stock.quantity)
            else:
                stockOut = int(stockOut) + int(stock.quantity)
        available  = stockIn - stockOut
        return available

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)
    type = models.CharField(max_length=2,choices=(('1','Stock-in'),('2','Stock-Out')), default = 1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.code + ' - ' + self.product.name

class Invoice(models.Model):
    transaction = models.CharField(max_length = 250)
    customer = models.CharField(max_length = 250)
    total = models.FloatField(default= 0)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.transaction

    def item_count(self):
        return Invoice_Item.objects.filter(invoice = self).aggregate(Sum('quantity'))['quantity__sum']

class Invoice_Item(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, blank= True, null= True)
    price = models.FloatField(default=0)
    quantity = models.FloatField(default=0)
    lotnumber = models.CharField(max_length=250, blank=True, null=True)
    expiry = models.CharField(max_length=250, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Set lotnumber and expiry based on the related Product
        if self.product:
            self.lotnumber = self.product.lotnumber
            self.expiry = self.product.expiry
        super().save(*args, **kwargs)

    def __str__(self):
        return self.invoice.transaction


@receiver(models.signals.post_save, sender=Invoice_Item)
def stock_update(sender, instance, **kwargs):
    stock = Stock(product = instance.product, quantity = instance.quantity, type = 2)
    stock.save()
    # stockID = Stock.objects.last().id
    Invoice_Item.objects.filter(id= instance.id).update(stock=stock)

@receiver(models.signals.post_delete, sender=Invoice_Item)
def delete_stock(sender, instance, **kwargs):
    try:
        stock = Stock.objects.get(id=instance.stock.id).delete()
    except:
        return instance.stock.id



    
    
