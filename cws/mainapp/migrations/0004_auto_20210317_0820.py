# Generated by Django 3.1.7 on 2021-03-17 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20210317_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='image',
            field=models.ImageField(upload_to='card_img/', verbose_name='Картинка карточки'),
        ),
    ]
