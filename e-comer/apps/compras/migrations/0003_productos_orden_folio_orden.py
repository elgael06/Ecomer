# Generated by Django 2.2.1 on 2019-05-25 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0002_auto_20190525_0408'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos_orden',
            name='folio_orden',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
