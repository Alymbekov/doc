# Generated by Django 2.2.1 on 2019-06-07 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imaster', '0003_auto_20190607_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, default='profile.jpg', null=True, upload_to='static/images'),
        ),
    ]
