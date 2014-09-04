# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lugar', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(help_text=b'Introduzca a\xc3\xb1o-mes-dia', verbose_name=b'Fecha de la encuesta')),
                ('ano', models.IntegerField(verbose_name=b'a\xc3\xb1o')),
                ('recolector', models.CharField(max_length=250, verbose_name=b'Nombre recolector de datos')),
                ('fecha2', models.DateField(verbose_name=b'Fecha de ingreso de la encuesta')),
                ('personas', models.CharField(max_length=250, verbose_name=b'Personas que introdujeron los datos')),
                ('oficina', models.CharField(max_length=50, verbose_name=b'Oficina de introducci\xc3\xb3n de datos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Finca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sexo', models.IntegerField(blank=True, null=True, verbose_name=b'Sexo del productor', choices=[(1, b'Mujer'), (3, b'Hombre')])),
                ('finca', models.CharField(help_text=b'Introduzca nombre de la finca', max_length=50, null=True, verbose_name=b'Nombre Finca', blank=True)),
                ('cedula_productor', models.CharField(help_text=b'Introduzca cedula del productor', max_length=25, null=True, blank=True)),
                ('area_finca', models.DecimalField(help_text=b'Introduzca el area de la finca en MZ', max_digits=10, decimal_places=2)),
                ('coordenadas_gps', models.DecimalField(decimal_places=6, max_digits=8, blank=True, help_text=b'Introduzca las coordenadas Latitud', null=True, verbose_name=b'Coordenadas Latitud')),
                ('coordenadas_lg', models.DecimalField(decimal_places=6, max_digits=8, blank=True, help_text=b'Introduzca las coordenadas Longitud', null=True, verbose_name=b'Coordenadas Longitud')),
                ('animal_bovino', models.IntegerField(help_text=b'Introduzca cuantos animales bovinos tiene')),
                ('animal_porcino', models.IntegerField(help_text=b'Introduzca cuantos animales porcinos tiene')),
                ('animal_equino', models.IntegerField(help_text=b'Introduzca cuantos animales equinos tiene')),
                ('animal_aves', models.IntegerField(help_text=b'Introduzca cuantas aves tiene')),
                ('animal_caprino', models.IntegerField(help_text=b'Introduzca cuantos animales caprino o pelibuey tiene')),
                ('tipo_casa', models.IntegerField(help_text=b'Introduzca que tipo de casa tiene', max_length=60, choices=[(1, b'Casa de madera rolliza con techo de paja'), (2, b'Casa de madera y techo de paja'), (3, b'Casa de madera con techo de zinc'), (4, b'Casa minifalda con techo de zinc'), (5, b'Casa de concreto con techo de zinc')])),
                ('area_casa', models.DecimalField(help_text=b'Introduzca area de la casa en pie cuadrado', max_digits=10, decimal_places=2)),
                ('fuente_agua', models.IntegerField(help_text=b'Introduzca que fuente de agua tiene', max_length=60, choices=[(1, b'Ojo de agua'), (2, b'Creeke'), (3, b'Pozo con brocal'), (4, b'Agua entubada'), (5, b'Pozo rustico'), (6, b'Agua por gravedad'), (7, b'Otros'), (8, b'Agua central certificado'), (9, b'Pozo rustico sin manejo')])),
                ('legalidad', models.IntegerField(help_text=b'Introduzca la legalidad de la propiedad', max_length=60, choices=[(1, b'Derecho real'), (2, b'Derecho procesorio'), (3, b'Promesa de venta'), (4, b'Titulo de reforma agraria'), (5, b'Titulo comunitario'), (6, b'Sin documentos'), (7, b'Escritura publica')])),
                ('propietario', models.CharField(help_text=b'Introduzca el propietario de la finca', max_length=50, choices=[(b'hombre', b'Hombre'), (b'mujer', b'Mujer'), (b'ambos', b'Ambos'), (b'parientes', b'Parientes')])),
                ('comunidad', models.ForeignKey(help_text=b'Introduzca nombre de la comunidad', to='lugar.Comunidad')),
                ('encuesta', models.ForeignKey(to='encuesta.Encuesta')),
                ('microcuenca', models.ForeignKey(help_text=b'Introduzca nombre de la microcuenca', to='lugar.Microcuenca')),
                ('municipio', models.ForeignKey(help_text=b'Introduzca nombre de la municipio', to='lugar.Municipio')),
            ],
            options={
                'ordering': ('finca',),
                'verbose_name': 'Datos generales de la familia socia',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Productores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250, verbose_name=b'Nombre y apellido')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='finca',
            name='nombre_productor',
            field=models.ForeignKey(to='encuesta.Productores'),
            preserve_default=True,
        ),
    ]
