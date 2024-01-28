# Generated by Django 4.2 on 2023-12-31 16:38

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("type", models.CharField(max_length=50)),
                ("payment_type", models.CharField(max_length=50)),
            ],
        ),
    ]
