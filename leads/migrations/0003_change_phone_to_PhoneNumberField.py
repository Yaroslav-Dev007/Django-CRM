# Generated by Django 2.1.2 on 2018-10-16 21:05

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_auto_20180410_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True),
        ),
    ]
