# Generated by Django 2.1 on 2018-08-09 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0003_auto_20180808_1518'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'ordering': ('id',)},
        ),
        migrations.AddField(
            model_name='libro',
            name='num_paginas',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]