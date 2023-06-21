# Generated by Django 4.0.6 on 2022-08-11 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sanchaykos', '0032_corevalues_ourteam_vision'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/projectsimg'),
        ),
        migrations.CreateModel(
            name='ProjectsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/projectsimg')),
                ('projectimg', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='sanchaykos.projects')),
            ],
        ),
    ]