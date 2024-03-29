# Generated by Django 5.0.3 on 2024-03-08 10:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.IntegerField(max_length=10)),
                ('special', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pateint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('mobile', models.IntegerField(max_length=10)),
                ('address', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctors')),
                ('pateint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.pateint')),
            ],
        ),
    ]
