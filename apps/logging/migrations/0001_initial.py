# Generated by Django 3.0.5 on 2020-04-20 19:05

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rest_framework_tracking', '0007_merge_20180419_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='APIRequestLog',
            fields=[
            ],
            options={
                'verbose_name': 'API request log',
                'verbose_name_plural': 'API request logs',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('rest_framework_tracking.apirequestlog',),
        ),
    ]
