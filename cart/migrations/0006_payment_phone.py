# Generated by Django 4.0.6 on 2022-09-14 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='phone',
            field=models.CharField(default='a', max_length=20),
        ),
    ]
