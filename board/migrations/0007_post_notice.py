# Generated by Django 4.1.5 on 2023-03-08 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_post_voter_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='notice',
            field=models.BooleanField(default=False),
        ),
    ]
