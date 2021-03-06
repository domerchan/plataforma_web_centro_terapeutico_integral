# Generated by Django 3.0.8 on 2020-09-09 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_merge_20200909_0323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='therapy_live',
            name='therapy_date',
        ),
        migrations.AddField(
            model_name='therapy_live',
            name='therapy_day',
            field=models.CharField(choices=[('MON', 'Lunes'), ('TUE', 'Martes'), ('WED', 'Miércoles'), ('THU', 'Jueves'), ('FRI', 'Viernes'), ('SAT', 'Sábado'), ('SUN', 'Domingo')], default='MON', max_length=3),
        ),
        migrations.AddField(
            model_name='therapy_live',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
