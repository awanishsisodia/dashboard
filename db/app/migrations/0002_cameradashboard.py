# Generated by Django 3.0.5 on 2020-11-29 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CameraDashboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nvr_dvr', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('sum_total_days_rec', models.PositiveIntegerField()),
                ('sum_of_baseline_days_rec', models.PositiveIntegerField()),
                ('sum_of_storage_warning', models.PositiveIntegerField()),
            ],
        ),
    ]
