# Generated by Django 3.2.13 on 2022-06-08 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original', models.FileField(blank=True, default=None, upload_to='originalVideos')),
                ('processed', models.FileField(blank=True, default=None, upload_to='processedVideos')),
            ],
        ),
    ]
