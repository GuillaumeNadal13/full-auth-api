# Generated by Django 4.2.1 on 2024-07-20 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('atomic_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('thickness', models.FloatField()),
                ('doped_percentage', models.FloatField(blank=True, null=True)),
                ('doped', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='samples.element')),
            ],
        ),
        migrations.CreateModel(
            name='SampleModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('prev_sample', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='samples.samplemodel')),
            ],
        ),
        migrations.CreateModel(
            name='SEMModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='SEM_images/')),
                ('description', models.TextField(blank=True, null=True)),
                ('magnification', models.BigIntegerField(blank=True, null=True)),
                ('voltage', models.FloatField(blank=True, null=True)),
                ('current', models.FloatField(blank=True, null=True)),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samples.samplemodel')),
            ],
            options={
                'verbose_name': 'SEM',
                'verbose_name_plural': 'SEMs',
            },
        ),
        migrations.CreateModel(
            name='Substrate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Company', models.CharField(max_length=100, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserMachineModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SEMModelFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='SEM_File/')),
                ('my_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='samples.semmodel')),
            ],
        ),
        migrations.AddField(
            model_name='samplemodel',
            name='substrate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='samples.substrate'),
        ),
        migrations.AddField(
            model_name='samplemodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samples.usermachinemodel'),
        ),
        migrations.CreateModel(
            name='LayerComposition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.FloatField()),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samples.element')),
                ('layer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samples.layer')),
            ],
        ),
        migrations.AddField(
            model_name='layer',
            name='substrate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='samples.substrate'),
        ),
    ]