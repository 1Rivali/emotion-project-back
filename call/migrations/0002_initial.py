# Generated by Django 4.2 on 2023-12-31 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("call", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="call",
            name="user_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_id",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
