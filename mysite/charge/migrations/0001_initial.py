# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-20 10:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('income', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ConsecutiveConsumeMission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.DecimalField(decimal_places=0, max_digits=4)),
                ('required_days', models.DecimalField(decimal_places=0, max_digits=4)),
                ('exp', models.DecimalField(decimal_places=0, max_digits=10)),
                ('money', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='ConsecutiveLoginMission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.DecimalField(decimal_places=0, max_digits=4)),
                ('required_days', models.DecimalField(decimal_places=0, max_digits=4)),
                ('exp', models.DecimalField(decimal_places=0, max_digits=10)),
                ('money', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('itemType', models.CharField(default='equipment', max_length=10)),
                ('attack', models.DecimalField(decimal_places=0, max_digits=5)),
                ('duration', models.DecimalField(decimal_places=0, default=0, max_digits=3)),
                ('expiredTime', models.DateTimeField(blank=True, default='0')),
                ('cost', models.DecimalField(decimal_places=0, default=0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='MealMission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal', models.CharField(max_length=20)),
                ('exp', models.DecimalField(decimal_places=0, max_digits=10)),
                ('money', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Missions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('missionType', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.DecimalField(decimal_places=0, max_digits=4)),
                ('hp', models.DecimalField(decimal_places=0, max_digits=4)),
                ('exp', models.DecimalField(decimal_places=0, max_digits=10)),
                ('money', models.DecimalField(decimal_places=0, max_digits=10)),
                ('pngFile', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RandomMission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=0, max_digits=10)),
                ('expiredTime', models.DateTimeField(blank=True)),
                ('exp', models.DecimalField(decimal_places=0, max_digits=10)),
                ('money', models.DecimalField(decimal_places=0, max_digits=10)),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charge.Missions')),
                ('targetItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charge.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spend', models.DecimalField(decimal_places=0, max_digits=10)),
                ('currency', models.CharField(max_length=10)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charge.Category')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.DecimalField(decimal_places=0, max_digits=3)),
                ('exp', models.DecimalField(decimal_places=0, max_digits=10)),
                ('max_exp', models.DecimalField(decimal_places=0, max_digits=10)),
                ('money', models.DecimalField(decimal_places=0, max_digits=12)),
                ('dps', models.DecimalField(decimal_places=0, default=1, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='User_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charge.Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charge.User')),
            ],
        ),
        migrations.CreateModel(
            name='User_Monster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_hp', models.DecimalField(decimal_places=0, max_digits=4)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('monster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charge.Monster')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charge.User')),
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
            model_name='record',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charge.User'),
        ),
        migrations.AddField(
            model_name='missions',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charge.User'),
        ),
        migrations.AddField(
            model_name='mealmission',
            name='mission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charge.Missions'),
        ),
        migrations.AddField(
            model_name='consecutiveloginmission',
            name='mission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charge.Missions'),
        ),
        migrations.AddField(
            model_name='consecutiveconsumemission',
            name='mission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charge.Missions'),
        ),
        migrations.AddField(
            model_name='consecutiveconsumemission',
            name='targetCategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charge.Category'),
        ),
    ]
