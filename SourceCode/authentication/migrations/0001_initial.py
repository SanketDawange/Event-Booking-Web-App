# Generated by Django 4.1.1 on 2022-11-22 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('host_name', models.CharField(max_length=50)),
                ('event_description', models.CharField(max_length=500)),
                ('event_date', models.DateField()),
                ('total_seats', models.IntegerField()),
                ('booked_seats', models.IntegerField()),
            ],
        ),
    ]
