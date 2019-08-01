# Generated by Django 2.2.3 on 2019-08-01 06:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_boardpost_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardpost',
            name='publish_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='boardpost',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='boardpost',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
