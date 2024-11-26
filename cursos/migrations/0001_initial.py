# Generated by Django 5.1.3 on 2024-11-25 16:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=255)),
                ('ciudad', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('cursos', models.ManyToManyField(related_name='estudiantes', to='cursos.curso')),
                ('direccion', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cursos.direccion')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('direccion', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cursos.direccion')),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='profesores',
            field=models.ManyToManyField(related_name='cursos', to='cursos.profesor'),
        ),
    ]