# Generated by Django 3.2.9 on 2021-12-10 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20211210_0614'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
