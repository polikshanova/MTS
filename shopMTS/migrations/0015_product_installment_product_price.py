# Generated by Django 4.0.5 on 2022-09-01 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopMTS', '0014_alter_product_availability'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='installment',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.CharField(default='', max_length=30),
        ),
    ]