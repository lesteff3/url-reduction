# Generated by Django 3.2.9 on 2022-07-09 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shorturl', '0003_auto_20220709_1415'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shorturl',
            old_name='long_url',
            new_name='original_url',
        ),
        migrations.RenameField(
            model_name='shorturl',
            old_name='short_url',
            new_name='reduction_url',
        ),
    ]