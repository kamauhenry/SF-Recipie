# Generated by Django 4.1.7 on 2023-03-27 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecipieApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cook',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, unique=True),
        ),
    ]