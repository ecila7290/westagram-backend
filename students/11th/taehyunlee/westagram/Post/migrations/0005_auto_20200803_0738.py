# Generated by Django 3.0.8 on 2020-08-03 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0004_auto_20200803_0452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.URLField(max_length=2000),
        ),
    ]