# Generated by Django 3.1.7 on 2021-03-25 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_remove_card_topic_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='order',
        ),
    ]
