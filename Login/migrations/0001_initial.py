# Generated by Django 3.1.5 on 2021-04-20 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listened_Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50, verbose_name='用户id')),
                ('lecture_id', models.CharField(max_length=20, verbose_name='讲座id')),
            ],
        ),
        migrations.CreateModel(
            name='Register_UserInfo',
            fields=[
                ('Username', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='用户名')),
                ('PassWord', models.CharField(max_length=20, verbose_name='用户密码')),
                ('PhoneNumber', models.CharField(max_length=15, verbose_name='用户电话')),
                ('Email', models.CharField(max_length=20, verbose_name='用户邮件')),
                ('nikename', models.CharField(max_length=30, verbose_name='用户昵称')),
            ],
        ),
        migrations.CreateModel(
            name='Reserved_Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maxNum', models.CharField(max_length=10, verbose_name='最大预约人数')),
                ('reservedNum', models.CharField(max_length=10, verbose_name='已预约人数')),
                ('user_id', models.CharField(max_length=50, verbose_name='用户id')),
                ('lecture_id', models.CharField(max_length=20, verbose_name='讲座id')),
            ],
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=60, verbose_name='用户token')),
                ('publish_power', models.CharField(max_length=10, verbose_name='发布权限')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Login.register_userinfo', verbose_name='用户id')),
            ],
        ),
        migrations.CreateModel(
            name='Published_Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture_id', models.CharField(max_length=20, verbose_name='讲座id')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Login.usertoken')),
            ],
        ),
    ]
