# Generated by Django 2.1.5 on 2019-03-28 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_auto_20190327_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsinfo',
            name='mian_pic',
            field=models.FileField(default='', upload_to='goods', verbose_name='广告图'),
        ),
    ]
