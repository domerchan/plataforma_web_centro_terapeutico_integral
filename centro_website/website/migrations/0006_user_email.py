# Generated by Django 3.0.8 on 2020-08-22 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20200822_0300'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=250, null=True),
        ),
    ]
