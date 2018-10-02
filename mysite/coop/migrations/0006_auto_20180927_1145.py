# Generated by Django 2.1.1 on 2018-09-27 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coop', '0005_auto_20180924_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='PresentationTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='presentation',
            name='topics',
        ),
        migrations.RemoveField(
            model_name='presentationfile',
            name='name',
        ),
        migrations.AddField(
            model_name='presentationfile',
            name='pres',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='coop.Presentation'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='presentation',
            name='file_dir',
            field=models.CharField(max_length=200, verbose_name='Presentation'),
        ),
        migrations.AddField(
            model_name='presentationtopic',
            name='presentation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coop.Presentation'),
        ),
        migrations.AddField(
            model_name='presentationtopic',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coop.Topic'),
        ),
    ]
