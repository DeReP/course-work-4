# Generated by Django 3.1.7 on 2021-04-17 07:05

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_auto_20210330_0820'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contentcard',
            old_name='topic_id',
            new_name='topic',
        ),
        migrations.AlterField(
            model_name='card',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='card_img/', verbose_name='Картинка карточки'),
        ),
    ]
