# Generated by Django 5.0.1 on 2024-02-04 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_alter_job_applicants'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='company_id',
            new_name='company',
        ),
    ]
