# Generated by Django 4.0.6 on 2022-08-11 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanchaykos', '0029_generalnotice_hrnotice_pressrelease_tendernotice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chairman',
            name='paragraph1',
        ),
        migrations.RemoveField(
            model_name='chairman',
            name='paragraph2',
        ),
        migrations.RemoveField(
            model_name='chairman',
            name='paragraph3',
        ),
        migrations.AddField(
            model_name='chairman',
            name='detailed_description',
            field=models.TextField(null=True),
        ),
    ]