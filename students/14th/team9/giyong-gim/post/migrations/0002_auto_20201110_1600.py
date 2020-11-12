# Generated by Django 3.1.3 on 2020-11-10 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='image_url',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='child',
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=400),
        ),
    ]
