# Generated by Django 2.2.1 on 2019-05-24 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Folio_proveedor', models.IntegerField()),
                ('productos', models.IntegerField()),
                ('Total', models.FloatField()),
                ('Descripcion', models.CharField(default='NA', max_length=100)),
                ('estatus', models.CharField(default='V', max_length=1)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('usuario_creo', models.IntegerField()),
                ('usuario_modifico', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Productos_orden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folio_producto', models.IntegerField()),
                ('costo', models.FloatField()),
                ('venta', models.FloatField()),
                ('iva', models.FloatField()),
                ('margen', models.FloatField()),
                ('Cantidad', models.FloatField()),
                ('Total', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=200)),
                ('RFC', models.CharField(default='X0X0X0X0X0X0', max_length=20)),
                ('Direccion', models.CharField(default='Conosido.', max_length=200)),
                ('Email', models.CharField(default='NA', max_length=50)),
                ('Telefono', models.CharField(max_length=10)),
                ('Representante', models.CharField(max_length=100)),
                ('Descripcion', models.CharField(default='NA', max_length=100)),
                ('estatus', models.CharField(default='V', max_length=1)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('usuario_creo', models.IntegerField()),
                ('usuario_modifico', models.IntegerField()),
            ],
        ),
    ]