# Generated by Django 3.0.8 on 2020-09-05 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_auto_20200904_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum_entry',
            name='description',
            field=models.TextField(max_length=5000),
        ),
    ]