# Generated by Django 4.0.5 on 2022-09-01 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopMTS', '0013_alter_product_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='availability',
            field=models.CharField(choices=[('Доступен в наличии', 'Доступен в наличии'), ('Предзаказ', 'Предзаказ')], max_length=50),
        ),
    ]
