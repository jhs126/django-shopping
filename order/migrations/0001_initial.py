# Generated by Django 2.1.5 on 2019-03-18 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0008_auto_20190316_1525'),
        ('goods', '0004_auto_20190310_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetailInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('count', models.IntegerField()),
                ('ogoods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('onumber', models.CharField(max_length=20)),
                ('odate', models.DateTimeField(auto_now=True)),
                ('oIsPay', models.BooleanField(default=False)),
                ('ototal', models.DecimalField(decimal_places=2, max_digits=8)),
                ('opostage', models.DecimalField(decimal_places=2, max_digits=4)),
                ('ocart', models.CharField(max_length=30)),
                ('oaddress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.AddressInfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='orderdetailinfo',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.OrderInfo'),
        ),
    ]