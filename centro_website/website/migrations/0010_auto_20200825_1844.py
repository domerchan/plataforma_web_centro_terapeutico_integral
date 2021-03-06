# Generated by Django 3.0.8 on 2020-08-25 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_disability_card'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='directory',
            name='direction',
        ),
        migrations.RemoveField(
            model_name='disability_card',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='forum_entry',
            name='representative',
        ),
        migrations.RemoveField(
            model_name='forum_response',
            name='entry',
        ),
        migrations.RemoveField(
            model_name='forum_response',
            name='user',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='representatives',
        ),
        migrations.RemoveField(
            model_name='relationship',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='relationship',
            name='representative',
        ),
        migrations.RemoveField(
            model_name='therapeutic_center',
            name='direction',
        ),
        migrations.RemoveField(
            model_name='therapy_live',
            name='therapist',
        ),
        migrations.RemoveField(
            model_name='therapy_local',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='therapy_local',
            name='therapist',
        ),
        migrations.DeleteModel(
            name='Tip',
        ),
        migrations.RemoveField(
            model_name='user',
            name='direction',
        ),
        migrations.DeleteModel(
            name='Direction',
        ),
        migrations.DeleteModel(
            name='Directory',
        ),
        migrations.DeleteModel(
            name='Disability_card',
        ),
        migrations.DeleteModel(
            name='Forum_entry',
        ),
        migrations.DeleteModel(
            name='Forum_response',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
        migrations.DeleteModel(
            name='Relationship',
        ),
        migrations.DeleteModel(
            name='Therapeutic_center',
        ),
        migrations.DeleteModel(
            name='Therapy_live',
        ),
        migrations.DeleteModel(
            name='Therapy_local',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
