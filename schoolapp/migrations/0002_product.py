# Generated by Django 5.0.2 on 2024-02-26 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_price', models.CharField(max_length=200)),
                ('product_quantity', models.IntegerField(max_length=200)),
            ],
        ),
    ]
