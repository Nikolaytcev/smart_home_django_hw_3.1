# Generated by Django 4.2.1 on 2023-05-24 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0003_alter_measurement_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='sensor_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='measurement.sensor'),
        ),
    ]
