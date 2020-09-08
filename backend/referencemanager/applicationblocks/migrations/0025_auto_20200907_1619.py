# Generated by Django 3.0.8 on 2020-09-07 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applicationblocks', '0024_auto_20200907_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reference',
            name='address',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='booktitle',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='eid',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='eprint',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='file',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='institution',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='journal',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='keywords',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='local_file',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='location',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='month',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='note',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='number',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='pages',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='publisher',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='series',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='url',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='volume',
        ),
    ]