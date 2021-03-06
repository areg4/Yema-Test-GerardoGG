# Generated by Django 3.1.13 on 2021-12-05 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pediatra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(max_length=500)),
                ('fechaHora', models.DateTimeField()),
                ('pediatra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Citas.pediatra')),
            ],
        ),
    ]
