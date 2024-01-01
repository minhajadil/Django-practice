# Generated by Django 5.0 on 2024-01-01 08:51

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Album', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicianDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Album_Name', models.CharField(max_length=40)),
                ('Rating', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1)),
                ('Release_date', models.DateField(default=django.utils.timezone.now)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Album.albumdb')),
            ],
        ),
    ]
