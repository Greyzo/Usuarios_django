# Generated by Django 4.2.1 on 2023-08-25 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_ciudad_alter_user_numerotelefonico_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='codigoPostal',
            field=models.IntegerField(),
        ),
    ]