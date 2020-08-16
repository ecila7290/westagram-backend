# Generated by Django 3.0.8 on 2020-08-13 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20200804_0204'),
        ('Posting', '0002_auto_20200804_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='liked_user',
            field=models.ManyToManyField(related_name='liked_user', to='User.User'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to='User.User'),
        ),
    ]