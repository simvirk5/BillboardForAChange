# Generated by Django 2.0.3 on 2018-06-07 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_auto_20180607_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
