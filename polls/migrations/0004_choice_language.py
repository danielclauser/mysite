# Generated by Django 4.0.4 on 2022-05-12 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_rename_question_2_choice_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='language',
            field=models.CharField(default=None, max_length=2),
        ),
    ]
