# Generated by Django 3.1.7 on 2021-05-05 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_comment'),
        ('questionapp', '0002_auto_20210429_0825'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='mainapp.topic', verbose_name='Тема'),
        ),
    ]
