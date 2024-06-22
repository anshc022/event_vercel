# Generated by Django 4.2.7 on 2024-06-18 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='team_size_info',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='member1_name',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='member1_vtu_number',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='member1_year',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='member2_name',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='member2_vtu_number',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='member2_year',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='member3_name',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='member3_vtu_number',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='member3_year',
        ),
        migrations.AddField(
            model_name='event',
            name='team_size',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='registration',
            name='members',
            field=models.JSONField(default=list),
        ),
    ]