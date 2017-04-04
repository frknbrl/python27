# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kullaniciAdi', models.CharField(max_length=50)),
                ('adi', models.CharField(max_length=50)),
                ('soyadi', models.CharField(max_length=50)),
                ('telefon', models.CharField(blank=True, max_length=50)),
                ('eposta', models.EmailField(blank=True, max_length=254)),
            ],
        ),
    ]
