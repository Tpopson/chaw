# Generated by Django 4.0.6 on 2022-09-16 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0011_alter_shopcart_c_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcart',
            name='c_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
