# Generated by Django 4.1.7 on 2023-02-16 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arana', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('pix', models.ImageField(upload_to='pix')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('year', models.IntegerField()),
                ('seats', models.IntegerField()),
                ('price', models.IntegerField()),
                ('promo_price', models.IntegerField(blank=True, null=True)),
                ('carimg', models.ImageField(upload_to='carimg')),
                ('uploaded_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('typee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arana.category')),
            ],
        ),
    ]