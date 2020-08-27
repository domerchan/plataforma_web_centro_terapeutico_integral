# Generated by Django 3.0.8 on 2020-08-26 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20200825_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tip',
            name='url',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='biography',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='degree',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='job_title',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number_2',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
