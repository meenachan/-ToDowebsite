# Generated by Django 3.0.8 on 2020-07-24 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_auto_20200723_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruits',
            name='title',
            field=models.TextField(blank=True),
        ),
    ]
