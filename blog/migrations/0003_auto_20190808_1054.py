# Generated by Django 2.0.2 on 2019-08-08 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_video_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='video_link',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
