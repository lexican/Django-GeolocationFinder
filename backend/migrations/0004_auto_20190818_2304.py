# Generated by Django 2.2.4 on 2019-08-18 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20190818_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='general_details',
            name='continent_code',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='general_details',
            name='continent_name',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
    ]