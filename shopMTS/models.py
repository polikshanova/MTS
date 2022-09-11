from django.db import models

class Product(models.Model):
    """
    model of product I-NET Shop MTS
    """
    CATEGORY_CHOICES = [
        ('Т', "Телефон"),
        ("Ч", "Часы"),
        ("Н", "Наушники")
    ]

    AVAILABILITY_CHOICES = [
        ('Доступен в наличии', "Доступен в наличии"),
        ("Предзаказ", "Предзаказ"),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='static', blank=True, null=True)
    availability = models.CharField(max_length=50, choices=AVAILABILITY_CHOICES)
    characteristics = models.TextField(max_length=150)
    price = models.CharField(max_length=30,default='')
    installment = models.CharField(max_length=30, default='')

    def __str__(self):
        return f'Товар: {self.name}'

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = 'Продукты'
