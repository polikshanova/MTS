# Generated by Django 4.0.5 on 2022-08-29 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopMTS', '0002_delete_qwe'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static'),
        ),
    ]
