# Generated by Django 4.2.1 on 2024-07-25 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0008_remove_layer_thickness'),
    ]

    operations = [
        migrations.CreateModel(
            name='LayerThickness',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('thickness', models.FloatField()),
                ('order', models.IntegerField()),
                ('Layers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samples.layer')),
            ],
        ),
        migrations.AlterField(
            model_name='substrate',
            name='Layers',
            field=models.ManyToManyField(to='samples.layerthickness'),
        ),
    ]
