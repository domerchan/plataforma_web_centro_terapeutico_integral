# Generated by Django 3.0.8 on 2020-08-11 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='identity_card',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='identity_card',
            field=models.IntegerField(),
        ),
    ]
