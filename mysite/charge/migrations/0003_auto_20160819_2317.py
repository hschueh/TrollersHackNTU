# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-19 23:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charge', '0002_auto_20160819_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.DecimalField(decimal_places=0, max_digits=4)),
                ('hp', models.DecimalField(decimal_places=0, max_digits=4)),
                ('exp', models.DecimalField(decimal_places=0, max_digits=4)),
                ('money', models.DecimalField(decimal_places=0, max_digits=4)),
                ('pngFile', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User_Monster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_hp', models.DecimalField(decimal_places=0, max_digits=4)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('monster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charge.Monster')),
            ],
        ),
        migrations.CreateModel(
            name='UserExp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.DecimalField(decimal_places=0, max_digits=4)),
                ('required_exp', models.DecimalField(decimal_places=0, max_digits=12)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='income',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='dps',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=5),
        ),
        migrations.AddField(
            model_name='user_monster',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charge.User'),
        ),
    ]
