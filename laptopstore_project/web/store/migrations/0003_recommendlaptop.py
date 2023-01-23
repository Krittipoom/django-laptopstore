# Generated by Django 4.1.5 on 2023-01-23 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_laptopsize_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecommendLaptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.laptop')),
            ],
        ),
    ]
