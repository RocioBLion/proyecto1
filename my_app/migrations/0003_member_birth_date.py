# Generated by Django 4.1.2 on 2022-10-26 17:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_rename_familymember_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='birth_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 10, 26, 17, 14, 49, 431265, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
