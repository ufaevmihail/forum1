# Generated by Django 3.1.1 on 2021-05-18 13:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myforum', '0013_auto_20210518_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='theme',
            name='last_update',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
