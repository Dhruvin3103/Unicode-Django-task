# Generated by Django 4.1.1 on 2022-09-24 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0005_rename_search_searchs'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchs',
            name='count',
            field=models.DecimalField(decimal_places=0, default=2, max_digits=100),
            preserve_default=False,
        ),
    ]
