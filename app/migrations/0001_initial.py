# Generated by Django 3.0.5 on 2020-05-02 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParkModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('comment', models.CharField(blank=True, max_length=200, null=True)),
                ('created_by', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'ParkModel',
                'verbose_name_plural': 'ParkModels',
            },
        ),
    ]