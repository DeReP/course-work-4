# Generated by Django 3.1.7 on 2021-03-25 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20210325_0729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='topic_id',
        ),
    ]