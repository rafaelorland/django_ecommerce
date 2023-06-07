# Generated by Django 4.2.1 on 2023-05-27 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_distribuidora'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='qtd',
            field=models.IntegerField(default=1, max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='distribuidora',
            field=models.CharField(blank=True, default='', max_length=140, null=True),
        ),
    ]
