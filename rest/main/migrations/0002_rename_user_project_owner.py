# Generated by Django 3.2.3 on 2021-06-30 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="user",
            new_name="owner",
        ),
    ]
