# Generated by Django 4.2.16 on 2024-11-09 21:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('iotUbs', '0002_remove_equipamentos_location_equipamentos_latitude_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_name', models.CharField(max_length=255)),
                ('temperature', models.FloatField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('status', models.CharField(max_length=50)),
                ('added_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
