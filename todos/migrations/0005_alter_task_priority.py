# Generated by Django 3.2 on 2023-01-27 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0004_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(default='lightblue', max_length=9),
        ),
    ]
