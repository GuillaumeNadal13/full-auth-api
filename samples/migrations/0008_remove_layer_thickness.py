# Generated by Django 4.2.1 on 2024-07-25 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0007_alter_layer_thickness'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='layer',
            name='thickness',
        ),
    ]
