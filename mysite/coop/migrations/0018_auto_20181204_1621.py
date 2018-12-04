# Generated by Django 2.1.1 on 2018-12-04 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coop', '0017_auto_20181202_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outreach',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Topic'),
        ),
        migrations.AddField(
            model_name='outreach',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='presentation',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='outreach',
            name='date',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='location',
            field=models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='people',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='outreach', to='coop.Person'),
        ),
        migrations.AlterField(
            model_name='person',
            name='bio',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True, verbose_name='Biography'),
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='author',
            field=models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='level',
            field=models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Level'),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='summary',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True, verbose_name='Summary'),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='topics',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='pres', to='coop.Topic'),
        ),
    ]
