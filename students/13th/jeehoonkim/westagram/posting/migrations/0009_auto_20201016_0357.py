# Generated by Django 3.1.1 on 2020-10-16 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0008_auto_20201016_0356'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postinglike',
            old_name='posting_id',
            new_name='posting',
        ),
        migrations.RenameField(
            model_name='postinglike',
            old_name='user_id',
            new_name='user',
        ),
    ]
