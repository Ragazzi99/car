# Generated by Django 4.1.7 on 2023-02-16 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arana', '0002_category_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
