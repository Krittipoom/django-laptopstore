# Generated by Django 4.1.5 on 2023-01-20 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptopsize',
            name='title',
            field=models.CharField(default='15.6', max_length=10, unique=True),
        ),
    ]