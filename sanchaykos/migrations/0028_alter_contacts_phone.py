# Generated by Django 4.0.6 on 2022-08-11 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanchaykos', '0027_alter_companynews_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
