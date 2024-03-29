# Generated by Django 2.2.6 on 2019-10-26 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(choices=[('Nissan', 'Nissan'), ('Toyota', 'Toyota'), ('Subaru', 'Subaru'), ('Mazda', 'Mazda'), ('Honda', 'Honda'), ('Mitsubishi', 'Mitsubishi'), ('Datsun', 'Datsun')], max_length=20)),
                ('year', models.IntegerField()),
                ('modelo', models.CharField(max_length=50)),
                ('motor', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('vendido', models.BooleanField()),
                ('imgFront', models.ImageField(upload_to='media')),
                ('imgSide', models.ImageField(upload_to='media')),
                ('imgBack', models.ImageField(upload_to='media')),
                ('imgInside', models.ImageField(upload_to='media')),
            ],
        ),
    ]
