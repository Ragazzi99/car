# Generated by Django 4.1.7 on 2023-02-16 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arana', '0004_product_color_product_registered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='registered',
            field=models.BooleanField(),
        ),
    ]