# Generated by Django 3.0.4 on 2020-03-24 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20200324_1812'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='category',
            new_name='subCategory',
        ),
        migrations.RenameField(
            model_name='organizer',
            old_name='category',
            new_name='subCategory',
        ),
        migrations.RenameField(
            model_name='plattform',
            old_name='category',
            new_name='subCategory',
        ),
    ]
