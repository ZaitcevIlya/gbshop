# Generated by Django 3.2.9 on 2021-11-27 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_products'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]