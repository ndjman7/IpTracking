# Generated by Django 2.1.2 on 2018-11-09 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0002_remove_httprequestinfo_visits'),
    ]

    operations = [
        migrations.AddField(
            model_name='httprequestinfo',
            name='memo',
            field=models.TextField(blank=True, verbose_name='메모'),
        ),
    ]