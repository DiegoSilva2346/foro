# Generated by Django 3.1.7 on 2021-04-10 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Temas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='titulo')),
                ('descripcion', models.CharField(max_length=100, verbose_name='descripcion')),
                ('texto', models.TextField()),
                ('fecha', models.DateTimeField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newtemas.categoria')),
            ],
            options={
                'verbose_name': 'Tema',
                'verbose_name_plural': 'Temas',
            },
        ),
        migrations.CreateModel(
            name='Visualizacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=100, verbose_name='descripcion')),
                ('id_tema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newtemas.temas')),
            ],
            options={
                'verbose_name': 'vizualisacion',
                'verbose_name_plural': 'visualizaciones',
            },
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=100, verbose_name='usuario')),
                ('fecha', models.DateTimeField()),
                ('respuesta', models.TextField()),
                ('id_tema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newtemas.temas')),
            ],
            options={
                'verbose_name': 'respuesta',
                'verbose_name_plural': 'respuestas',
            },
        ),
    ]
