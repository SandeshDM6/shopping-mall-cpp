# Generated by Django 3.2.16 on 2023-04-26 20:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('shoppingapp', '0005_job_picture'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Job',
            new_name='Shop',
        ),
    ]
