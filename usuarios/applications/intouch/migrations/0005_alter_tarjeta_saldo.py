# Generated by Django 4.2.4 on 2023-08-27 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intouch', '0004_alter_tarjeta_saldo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarjeta',
            name='saldo',
            field=models.FloatField(default=7000),
        ),
    ]