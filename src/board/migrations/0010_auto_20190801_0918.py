# Generated by Django 2.2.3 on 2019-08-01 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0009_boardpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]