# Generated by Django 3.0.8 on 2020-08-11 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20200810_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='direction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='website.Direction'),
        ),
    ]
