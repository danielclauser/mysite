# Generated by Django 4.0.4 on 2022-05-12 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='question',
            new_name='question_2',
        ),
    ]
