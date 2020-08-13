# Generated by Django 3.0.8 on 2020-08-04 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='date',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
