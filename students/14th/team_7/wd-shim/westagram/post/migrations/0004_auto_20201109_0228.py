# Generated by Django 3.1.3 on 2020-11-08 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20201108_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='img_url',
            field=models.CharField(max_length=500),
        ),
    ]