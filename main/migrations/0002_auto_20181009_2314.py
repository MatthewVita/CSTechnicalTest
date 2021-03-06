# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-09 23:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.CharField(max_length=64)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Thing',
        ),
        migrations.AddField(
            model_name='comment',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main.Topic'),
        ),
    ]
