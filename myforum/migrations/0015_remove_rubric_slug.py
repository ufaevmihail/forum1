# Generated by Django 3.1.1 on 2021-05-20 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myforum', '0014_auto_20210518_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rubric',
            name='slug',
        ),
    ]