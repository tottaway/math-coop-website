# Generated by Django 2.1.1 on 2018-12-04 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coop', '0018_auto_20181204_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='pres',
        ),
    ]
