# Generated by Django 2.0.6 on 2018-07-18 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseware', '0009_auto_20180717_1500'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapters',
            old_name='parent_course',
            new_name='course',
        ),
    ]
