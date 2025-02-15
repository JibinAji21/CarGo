# Generated by Django 5.1.4 on 2025-02-12 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_id', models.TextField()),
                ('car_name', models.TextField()),
                ('car_year', models.IntegerField()),
                ('car_place', models.TextField()),
                ('car_rent', models.IntegerField()),
                ('car_fuel', models.TextField()),
                ('car_img', models.FileField(upload_to='')),
            ],
        ),
    ]
