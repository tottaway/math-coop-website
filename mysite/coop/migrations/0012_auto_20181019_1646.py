# Generated by Django 2.1.1 on 2018-10-19 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coop', '0011_presentation_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outreach',
            name='id',
        ),
        migrations.RemoveField(
            model_name='person',
            name='id',
        ),
        migrations.RemoveField(
            model_name='presentation',
            name='id',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='id',
        ),
        migrations.AlterField(
            model_name='outreach',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='name',
            field=models.CharField(max_length=200, primary_key=True, serialize=False, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Topic'),
        ),
    ]
