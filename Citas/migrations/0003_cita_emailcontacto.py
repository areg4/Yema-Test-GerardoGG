# Generated by Django 3.1.13 on 2021-12-06 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Citas', '0002_auto_20211204_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='cita',
            name='emailContacto',
            field=models.EmailField(default='areg_4@hotmail.com', max_length=254),
            preserve_default=False,
        ),
    ]
