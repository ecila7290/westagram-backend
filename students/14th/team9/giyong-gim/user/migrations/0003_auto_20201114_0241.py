# Generated by Django 3.1.3 on 2020-11-14 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20201113_0533'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_created',
            new_name='created_at',
        ),
    ]
