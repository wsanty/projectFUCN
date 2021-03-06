# Generated by Django 2.1 on 2018-08-30 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profesion', models.CharField(max_length=50, verbose_name='Título profesional')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('E', 'Estudiante'), ('A', 'Asesor')], max_length=1)),
                ('primer_apellido', models.CharField(max_length=20, verbose_name='Primer Apellido')),
                ('segundo_apellido', models.CharField(max_length=20, verbose_name='Segundo Apellido')),
                ('nombres', models.CharField(max_length=30, verbose_name='Nombres')),
                ('identificacion', models.CharField(max_length=10, verbose_name='Número de Identificación')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo Electrónico')),
                ('telefono', models.CharField(max_length=10, verbose_name='Número Telefónico')),
            ],
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True, verbose_name='Código del Programa')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre de Programa')),
                ('decanatura', models.CharField(max_length=30, verbose_name='Facultad')),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True, verbose_name='Código Proyecto')),
                ('nombre', models.CharField(max_length=60, verbose_name='Nombre del Proyecto')),
                ('descripcion', models.TextField(max_length=250, verbose_name='Descripción Corta del Proyecto')),
                ('tema', models.CharField(max_length=80, verbose_name='Tema del proyecto')),
                ('fecha_inicio', models.DateField(auto_now_add=True, verbose_name='Fecha Inicio')),
                ('fecha_fin', models.DateField(auto_now_add=True, verbose_name='Fecha Fin')),
                ('estado', models.CharField(choices=[('AB', 'Abierto'), ('CE', 'Cerrado'), ('AN', 'Anulado'), ('AP', 'Aprobado'), ('RE', 'Rechazado'), ('DE', 'Destacado')], max_length=2)),
                ('integrantes', models.ManyToManyField(to='GestionProyectos.Persona')),
            ],
        ),
        migrations.AddField(
            model_name='persona',
            name='programa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionProyectos.Programa'),
        ),
        migrations.AddField(
            model_name='asesor',
            name='asesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionProyectos.Persona'),
        ),
    ]
