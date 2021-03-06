# Generated by Django 3.0.3 on 2020-08-12 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(max_length=250)),
                ('text', models.CharField(max_length=200)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.User')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Posting.Posting')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.User')),
            ],
        ),
    ]
