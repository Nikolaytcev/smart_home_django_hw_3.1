# Generated by Django 4.2.1 on 2023-05-24 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0006_alter_measurement_sensor_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='sensor_id',
            new_name='sensor',
        ),
    ]