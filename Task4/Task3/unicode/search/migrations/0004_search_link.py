# Generated by Django 4.1.1 on 2022-09-24 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_search_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='link',
            field=models.TextField(default=''),
        ),
    ]