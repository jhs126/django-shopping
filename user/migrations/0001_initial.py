# Generated by Django 2.1.5 on 2019-03-10 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=40)),
                ('uemail', models.CharField(max_length=30)),
                ('ufullname', models.CharField(max_length=20)),
                ('uaddress', models.CharField(max_length=100)),
                ('uzipcode', models.CharField(max_length=6)),
                ('utel', models.CharField(max_length=11)),
            ],
        ),
    ]
