# Generated by Django 4.1.5 on 2023-04-12 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0023_post_file_alter_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='file',
        ),
    ]
