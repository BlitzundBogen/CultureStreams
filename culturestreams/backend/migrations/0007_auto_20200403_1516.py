# Generated by Django 3.0.4 on 2020-04-03 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20200403_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='subCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.SubCategory'),
        ),
    ]
