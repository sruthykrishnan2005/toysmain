# Generated by Django 5.1.3 on 2024-12-17 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_cart_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='Category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='building',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='dolls',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='rideonvehicles',
            field=models.TextField(blank=True, null=True),
        ),
    ]
