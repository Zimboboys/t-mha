# Generated by Django 3.0.5 on 2020-05-31 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0012_auto_20200531_1007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='cat',
        ),
        migrations.AddField(
            model_name='event',
            name='cat_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
