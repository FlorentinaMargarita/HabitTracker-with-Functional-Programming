# Generated by Django 3.1.4 on 2021-01-02 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0041_auto_20210101_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='count',
            name='start_time',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
