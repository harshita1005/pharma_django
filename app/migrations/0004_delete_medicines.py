# Generated by Django 4.0.4 on 2022-08-06 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_medicine_image_medicines_medicinei'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Medicines',
        ),
    ]