# Generated by Django 2.0.2 on 2019-08-08 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_video_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='video_link',
        ),
    ]