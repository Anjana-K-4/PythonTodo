# Generated by Django 3.2.16 on 2022-12-03 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1997-07-04'),
            preserve_default=False,
        ),
    ]
