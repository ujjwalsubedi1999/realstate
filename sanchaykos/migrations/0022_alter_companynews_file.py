# Generated by Django 4.0.6 on 2022-08-09 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanchaykos', '0021_alter_companynews_description_alter_companynews_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companynews',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='static/companynewsfile'),
        ),
    ]