# Generated by Django 4.1 on 2022-08-29 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_rename_is_done_task_is_archived'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.TextField(blank=True),
        ),
    ]