# Generated by Django 3.0.7 on 2020-06-20 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker', '0005_auto_20200618_0221'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='operating_system',
            field=models.CharField(choices=[('windows', 'Windows'), ('linux', 'Linux'), ('mac', 'Mac'), ('android', 'Android'), ('ios', 'ios')], default='windows', max_length=7),
        ),
    ]