# Generated by Django 2.2.2 on 2019-06-24 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0015_auto_20190604_1830"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="has_marketing_access",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="has_sales_access",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="comment",
            name="lead",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="leads_comments",
                to="leads.Lead",
            ),
        ),
    ]
