# Generated by Django 2.1.5 on 2019-03-16 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_addressinfo_auser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='addressInfo',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='uaddress',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='ufullname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='utel',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='uzipcode',
            field=models.CharField(default='', max_length=6),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uemail',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='upwd',
            field=models.CharField(default='', max_length=40),
        ),
    ]
