# Generated by Django 3.2.6 on 2023-05-27 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='distribuidora',
            field=models.CharField(default=3, max_length=120),
            preserve_default=False,
        ),
    ]