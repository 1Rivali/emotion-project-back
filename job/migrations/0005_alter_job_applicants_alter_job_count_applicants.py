# Generated by Django 5.0.1 on 2024-02-10 18:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("job", "0004_rename_company_id_job_company"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="applicants",
            field=models.ManyToManyField(
                blank=True, null=True, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="job",
            name="count_applicants",
            field=models.IntegerField(default=0),
        ),
    ]
