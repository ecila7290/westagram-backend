# Generated by Django 3.1.2 on 2020-10-10 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='description',
            field=models.TextField(null=True),
        ),
    ]