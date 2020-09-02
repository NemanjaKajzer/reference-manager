# Generated by Django 3.0.8 on 2020-09-01 16:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('applicationblocks', '0013_auto_20200901_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reference',
            name='editor',
            field=models.ManyToManyField(default=None, related_name='editor_id', related_query_name='editor_id', to=settings.AUTH_USER_MODEL),
        ),
    ]