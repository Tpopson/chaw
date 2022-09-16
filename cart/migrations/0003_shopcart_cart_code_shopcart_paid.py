# Generated by Django 4.0.6 on 2022-08-31 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_shopcart_options_alter_shopcart_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcart',
            name='cart_code',
            field=models.CharField(default='a', max_length=255),
        ),
        migrations.AddField(
            model_name='shopcart',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
