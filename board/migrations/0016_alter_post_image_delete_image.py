# Generated by Django 4.1.5 on 2023-04-03 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0015_alter_post_voter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/{{Post.category.description}}/{{Post.id}}/'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
