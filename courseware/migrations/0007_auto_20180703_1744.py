# Generated by Django 2.0.6 on 2018-07-03 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courseware', '0006_auto_20180703_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachingelementbase',
            name='chapter',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='courseware.Chapters'),
        ),
    ]