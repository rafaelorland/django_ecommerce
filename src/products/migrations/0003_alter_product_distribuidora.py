# Generated by Django 4.2.1 on 2023-05-27 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_distribuidora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='distribuidora',
            field=models.CharField(blank=True, default='DEFAULT VALUE', max_length=140, null=True),
        ),
    ]
