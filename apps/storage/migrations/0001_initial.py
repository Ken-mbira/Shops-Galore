# Generated by Django 3.2.9 on 2021-12-15 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('delivery', '0005_alter_destination_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='storage_facility', to='delivery.location')),
            ],
        ),
    ]
