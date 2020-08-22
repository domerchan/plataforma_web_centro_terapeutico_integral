# Generated by Django 3.0.8 on 2020-08-11 04:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_street', models.CharField(max_length=250)),
                ('secondary_street', models.CharField(max_length=250, null=True)),
                ('house_number', models.CharField(max_length=5, null=True)),
                ('reference', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Disability_card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disability', models.CharField(choices=[('HE', 'Discapacidad Auditiva'), ('PH', 'Discapacidad Física'), ('IN', 'Discapacidad Intelectual'), ('LA', 'Discapacidad del Lenguaje'), ('PS', 'Discapacidad Psicosocial'), ('VI', 'Discapacidad Visual')], max_length=2)),
                ('disability_description', models.TextField()),
                ('disability_percentage', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('identity_card', models.IntegerField(max_length=10)),
                ('birth', models.DateField()),
                ('sex', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M', max_length=1)),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('country_origin', models.CharField(max_length=150)),
                ('province', models.CharField(max_length=100)),
                ('canton', models.CharField(max_length=100)),
                ('educational_institution_type', models.CharField(choices=[('IN', 'Inclusiva'), ('SP', 'Especializada'), ('RE', 'Regular')], default='SP', max_length=2)),
                ('educational_institution', models.CharField(max_length=400)),
                ('parish_type', models.CharField(choices=[('UB', 'Urbana'), ('RU', 'Rural')], default='UB', max_length=2)),
                ('bond_desarrollo_humano', models.BooleanField()),
                ('bond_joaquin_gallegos', models.BooleanField()),
                ('alimony', models.BooleanField()),
                ('jubilee_pension', models.BooleanField()),
                ('montepio', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('identity_card', models.IntegerField(max_length=10)),
                ('rol', models.CharField(choices=[('AD', 'Administrador'), ('TR', 'Terapeuta'), ('RP', 'Representante')], default='RP', max_length=2)),
                ('birth', models.DateField()),
                ('sex', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M', max_length=1)),
                ('civil_status', models.CharField(max_length=150)),
                ('phone_number_1', models.PositiveIntegerField()),
                ('phone_number_2', models.PositiveIntegerField()),
                ('job_title', models.CharField(max_length=500)),
                ('degree', models.CharField(max_length=500)),
                ('biography', models.TextField()),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='website.Direction')),
            ],
        ),
        migrations.CreateModel(
            name='Representative_Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relationship', models.CharField(max_length=100)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Patient')),
                ('representative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.User')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='representatives',
            field=models.ManyToManyField(through='website.Representative_Patient', to='website.User'),
        ),
    ]