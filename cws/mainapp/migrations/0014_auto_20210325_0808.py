# Generated by Django 3.1.7 on 2021-03-25 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_auto_20210325_0741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='topic_id',
            new_name='topic',
        ),
    ]
