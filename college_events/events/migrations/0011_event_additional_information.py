# Generated by Django 4.2.7 on 2024-06-21 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_remove_event_dates_and_deadlines_event_event_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='additional_information',
            field=models.TextField(default='All participants will receive a Participation Certificate.\nWinners will receive a Merit Certificate.\nAll participants will receive On-Duty (OD) status.'),
        ),
    ]
