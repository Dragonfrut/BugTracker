# Generated by Django 3.0.5 on 2020-04-24 18:22

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=djrichtextfield.models.RichTextField(blank=True, null=True),
        ),
    ]
