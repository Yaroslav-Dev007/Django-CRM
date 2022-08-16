# Generated by Django 3.2.11 on 2022-07-14 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0019_auto_20211022_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='close_date',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='organization',
            field=models.CharField(max_length=255, null=True, verbose_name='Organization'),
        ),
        migrations.AddField(
            model_name='lead',
            name='probability',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
