from django.db import models

# Create your models here.
class Product(models.Model):
    """
    model of product I-NET Shop MTS
    """
    CATEGORY_CHOICES = [
        ('Т', "Телефон"),
        ("Ч", "Часы"),
        ("Н","Наушники")
    ]

    AVAILABILITY_CHOICES = [
        ('Д', "Доступен в наличии"),
        ("П","Предзаказ")
    ]
    category = models.CharField(choices=CATEGORY_CHOICES),
    vendor = models.CharField(max_length=10),
    image = models.ImageField(upload_to='static/posts'), #### заменить!!!
    availability = models.CharField(choices=AVAILABILITY_CHOICES),
    characteristics = models.TextField(max_length=150)

class User(models.Model):
    """
    model of users of I-NET Shop MTS
    """

    name = models.CharField(max_length=50),
    email = models.CharField(max_length=50),
    number = models.CharField(max_length=13),
    password = models.CharField(max_length=50)