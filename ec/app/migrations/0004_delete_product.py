# Generated by Django 4.2.3 on 2023-07-09 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_product_discounted_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]
