# Generated by Django 3.0.4 on 2020-04-29 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0030_event_donationlink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.URLField(blank=True, max_length=250, null=True, verbose_name='Bild'),
        ),
    ]