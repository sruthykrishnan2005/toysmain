# Generated by Django 5.1.4 on 2024-12-17 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='building',
        ),
        migrations.RemoveField(
            model_name='product',
            name='dolls',
        ),
        migrations.RemoveField(
            model_name='product',
            name='rideonvehicles',
        ),
    ]