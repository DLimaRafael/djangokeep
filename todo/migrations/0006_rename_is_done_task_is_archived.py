# Generated by Django 4.1 on 2022-08-15 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_alter_task_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='is_done',
            new_name='is_archived',
        ),
    ]