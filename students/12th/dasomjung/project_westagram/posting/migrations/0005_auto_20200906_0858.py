# Generated by Django 3.1 on 2020-09-06 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0004_auto_20200906_0752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posting',
            name='images_url',
        ),
        migrations.AddField(
            model_name='images',
            name='posting',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posting.posting'),
        ),
    ]
