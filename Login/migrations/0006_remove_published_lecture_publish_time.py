# Generated by Django 3.1.5 on 2021-05-04 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0005_published_lecture_publish_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='published_lecture',
            name='publish_time',
        ),
    ]
