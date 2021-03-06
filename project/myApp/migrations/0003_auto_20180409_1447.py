# Generated by Django 2.0.3 on 2018-04-09 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_auto_20180409_1129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.IntegerField()),
                ('productimg', models.CharField(max_length=255)),
                ('productname', models.CharField(max_length=255)),
                ('productlongname', models.CharField(max_length=255)),
                ('isxf', models.CharField(max_length=255)),
                ('pmdesc', models.CharField(max_length=255)),
                ('specifics', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('marketprice', models.CharField(max_length=255)),
                ('categoryid', models.IntegerField()),
                ('childcid', models.IntegerField()),
                ('childcidname', models.CharField(max_length=255)),
                ('dealerid', models.IntegerField()),
                ('storenums', models.IntegerField()),
                ('productnum', models.IntegerField()),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'goods',
            },
        ),
        migrations.CreateModel(
            name='Wheel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('trackid', models.CharField(max_length=100)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'wheel',
            },
        ),
        migrations.AlterModelTable(
            name='mustbuy',
            table='must_buy',
        ),
        migrations.AlterModelTable(
            name='nav',
            table='nav',
        ),
    ]
