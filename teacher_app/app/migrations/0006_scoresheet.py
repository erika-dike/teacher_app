# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 12:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_student_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScoreSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_last_modified', models.DateTimeField(auto_now=True)),
                ('score', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score', to='app.Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Subject')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
