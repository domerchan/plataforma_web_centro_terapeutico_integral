# Generated by Django 3.0.7 on 2020-09-07 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_auto_20200905_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='image',
            field=models.FileField(null=True, upload_to='images/', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='therapy_local',
            name='therapist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.User'),
        ),
        migrations.AlterField(
            model_name='therapy_local',
            name='therapy_date',
            field=models.CharField(max_length=500),
        ),
    ]
