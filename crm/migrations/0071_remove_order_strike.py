# Generated by Django 3.1.4 on 2021-01-05 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0070_auto_20210104_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='strike',
        ),
    ]
