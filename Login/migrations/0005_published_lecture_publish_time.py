# Generated by Django 3.1.5 on 2021-05-04 17:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0004_remove_published_lecture_publish_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='published_lecture',
            name='publish_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]