# Generated by Django 2.2.1 on 2019-05-28 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion_caja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folio_asignacion', models.IntegerField()),
                ('efectivo', models.FloatField()),
                ('cheques', models.FloatField()),
                ('vouchers', models.FloatField()),
                ('total', models.FloatField()),
                ('total_corte', models.FloatField()),
                ('diferencia', models.FloatField()),
                ('usuario_creo', models.IntegerField()),
                ('usuario_modifico', models.IntegerField()),
                ('estatus', models.CharField(max_length=1)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto_ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folio_ticket', models.IntegerField()),
                ('folio_producto', models.IntegerField()),
                ('camtidad', models.IntegerField()),
                ('total', models.FloatField()),
                ('descuento', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folio_asignacion', models.IntegerField()),
                ('productos', models.IntegerField()),
                ('total', models.FloatField()),
                ('descuento', models.FloatField()),
                ('folio_cliente', models.IntegerField()),
                ('estatus', models.CharField(max_length=1)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('hora', models.DateTimeField(auto_now_add=True)),
                ('tipo_pago', models.CharField(max_length=2)),
            ],
        ),
    ]