# Generated by Django 4.0.4 on 2022-08-29 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_anel_caminho'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anel',
            name='caminho',
            field=models.CharField(default=None, max_length=100, verbose_name='Caminho'),
        ),
    ]