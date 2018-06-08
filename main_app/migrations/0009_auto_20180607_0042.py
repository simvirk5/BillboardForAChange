# Generated by Django 2.0.3 on 2018-06-07 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20180606_2258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_text',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='inspiration',
            field=models.TextField(),
        ),
    ]