# The Sensmieux Inventory System is a customizable inventory system, based on Django.  While it is intended for a medical distributor business, the system is open for everyone to try and modify. Just follow the instructions below:
#
#
# Unzip the static.zip file
#
# Application Packages to Install
# python3-pip
# python3-venv
# libmysqlclient-dev
# python3-bottle
# xampp
# 
# 
# Go to phpMyAdmin (127.0.0.1/phpMyAdmin in your browser)  and 
# create new database named "sensmieux_django"
# 
# 
# How to Set Up Virtual Environment in Command Line (after directing the command prompt to the directory just outside the "sensmieux" folder:
# python3 -m venv my_env #assign virtual environment
# source my_env/bin/activate #always perform this to enter the virtual environment  before making any django/python commands
# 
# 
# 
# Python Pip Packages to Install (After setting up Virtual Ennvironment, type "pip install package" - replace package with the package name below):
# django
# mysqlclient
# pillow
# cryptography
# django-crispy-forms
# crispy-bootstrap5
# 
# 
# to complete the database migration, change directory to the root sensmieux folder. and type the command
# python3 manage.py makemigrations
# python3 manage.py migrate
# python3 manage.py createsuperuser #creates a superuser account
# 
# 
# 
# MYSQL ROUTINES TO CREATE in phpMyAdmin
# 
# ----------------------------------------------
# Routine name: listexpirydates
# Type: PROCEDURE
# Definition:
# 
# BEGIN
#     SELECT expiry, name FROM inventorysystem_product ORDER BY expiry;
# END
# 
# Definer: root@localhost
# ----------------------------------------------
# 
# ----------------------------------------------
# Routine name: pricelist
# Type: PROCEDURE
# Definition:
# 
# BEGIN
#     SELECT name, price FROM inventorysystem_product ORDER BY name;
# END
# 
# Definer: root@localhost
# ----------------------------------------------
# 
# 
# AFTER COMPLETING PREREQUISITES, type the command:
# python3 manage.py runserver
# 
# go to 127.0.0.1:8000 in your browser and log-in using the superuser account that you created earlier.
# Happy customizing!
