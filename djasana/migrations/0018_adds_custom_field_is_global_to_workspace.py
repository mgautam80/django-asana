# Generated by Django 2.1.7 on 2019-07-12 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djasana', '0017_adds_project_due_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='customfield',
            name='is_global_to_workspace',
            field=models.BooleanField(default=False),
        ),
    ]
