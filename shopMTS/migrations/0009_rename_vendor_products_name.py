# Generated by Django 4.0.5 on 2022-08-30 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopMTS', '0008_alter_products_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='vendor',
            new_name='name',
        ),
    ]
