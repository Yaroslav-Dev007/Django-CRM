# Generated by Django 2.2.10 on 2020-04-27 12:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0021_document_company"),
        ("cases", "0004_case_teams"),
    ]

    operations = [
        migrations.AddField(
            model_name="case",
            name="company",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="common.Company",
            ),
        ),
    ]
