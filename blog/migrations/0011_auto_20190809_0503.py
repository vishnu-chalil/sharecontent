# Generated by Django 2.2.4 on 2019-08-09 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
