# Generated by Django 3.1.3 on 2020-11-10 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0004_remove_post_updated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='image_url',
        ),
    ]
