# Generated by Django 4.0.6 on 2022-08-09 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanchaykos', '0019_projects'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, null=True)),
                ('description', models.TextField(null=True)),
                ('file', models.FileField(null=True, upload_to='companynewsfile')),
            ],
        ),
    ]
