# Generated by Django 3.1.4 on 2021-01-02 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0042_auto_20210101_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='count',
            name='start_time',
        ),
    ]
