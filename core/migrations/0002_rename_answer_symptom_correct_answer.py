# Generated by Django 3.2.13 on 2024-05-23 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='symptom',
            old_name='answer',
            new_name='correct_answer',
        ),
    ]
