# Generated by Django 2.0.2 on 2019-08-08 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_video_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video_link',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
