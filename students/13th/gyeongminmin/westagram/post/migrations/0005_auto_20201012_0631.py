# Generated by Django 3.1.1 on 2020-10-12 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20201012_0629'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='comment_id',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='post_id',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='postimage',
            old_name='post_id',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='postlikes',
            old_name='post_id',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='postlikes',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='posts',
            old_name='user_id',
            new_name='user',
        ),
    ]
