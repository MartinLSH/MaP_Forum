# Generated by Django 4.1.5 on 2023-03-11 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_post_notice'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='view_cnt',
            field=models.BigIntegerField(default=0),
        ),
    ]
