# Generated by Django 3.2.3 on 2021-06-30 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_user_project_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_name',
            field=models.CharField(default='Project', max_length=100),
            preserve_default=False,
        ),
    ]