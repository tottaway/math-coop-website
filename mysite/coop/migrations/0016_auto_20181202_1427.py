# Generated by Django 2.1.1 on 2018-12-02 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coop', '0015_auto_20181019_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personoutreach',
            name='outreach',
        ),
        migrations.RemoveField(
            model_name='personoutreach',
            name='person',
        ),
        migrations.RemoveField(
            model_name='presentationtopic',
            name='presentation',
        ),
        migrations.RemoveField(
            model_name='presentationtopic',
            name='topic',
        ),
        migrations.AddField(
            model_name='outreach',
            name='people',
            field=models.ManyToManyField(related_name='outreach', to='coop.Person'),
        ),
        migrations.AddField(
            model_name='presentation',
            name='topics',
            field=models.ManyToManyField(related_name='pres', to='coop.Topic'),
        ),
        migrations.DeleteModel(
            name='PersonOutreach',
        ),
        migrations.DeleteModel(
            name='PresentationTopic',
        ),
    ]
