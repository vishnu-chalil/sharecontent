# Generated by Django 2.0.2 on 2019-08-08 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190808_1110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='video_link',
        ),
    ]
