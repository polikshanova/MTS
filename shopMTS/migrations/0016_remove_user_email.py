# Generated by Django 4.0.5 on 2022-09-05 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopMTS', '0015_product_installment_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
    ]
