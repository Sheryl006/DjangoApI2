# Generated by Django 5.0.6 on 2024-08-14 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='uploads/images/profile.jpg', upload_to='uploads/images')),
                ('name', models.CharField(max_length=150)),
                ('manufacturer', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='uploads/images/profile.jpg', upload_to='uploads/images')),
                ('name', models.CharField(max_length=150)),
                ('manufacturer', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='YourModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
    ]