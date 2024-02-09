# Generated by Django 5.0.2 on 2024-02-09 05:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_rename_photo_taskdetails_photos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskdetails',
            name='photos',
        ),
        migrations.AddField(
            model_name='photo',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.taskdetails'),
        ),
    ]