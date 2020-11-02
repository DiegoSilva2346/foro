# Generated by Django 3.1 on 2020-11-01 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newtemas', '0006_auto_20201004_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temas',
            name='descripcion',
            field=models.CharField(max_length=100, verbose_name='descripcion'),
        ),
        migrations.AlterField(
            model_name='temas',
            name='elige_tu_categoria',
            field=models.IntegerField(blank=True, choices=[(1, 'pasteles'), (2, 'Deportes'), (3, 'Ciencia'), (4, 'Clima'), (5, 'Pandemia'), (6, 'Programaciòn')], default=2),
        ),
        migrations.AlterField(
            model_name='temas',
            name='titulo',
            field=models.CharField(max_length=50, verbose_name='titulo'),
        ),
    ]
