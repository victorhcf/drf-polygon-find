# Generated by Django 4.2.3 on 2023-07-12 15:35

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suppliersarea', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicearea',
            name='information',
            field=django.contrib.gis.db.models.fields.PolygonField(default=None, srid=4326),
            preserve_default=False,
        ),
    ]