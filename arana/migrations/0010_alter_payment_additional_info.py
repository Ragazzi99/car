# Generated by Django 4.1.7 on 2023-03-29 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arana', '0009_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='additional_info',
            field=models.TextField(),
        ),
    ]
