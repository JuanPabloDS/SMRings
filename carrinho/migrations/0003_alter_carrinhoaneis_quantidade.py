# Generated by Django 4.0.4 on 2022-08-18 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrinho', '0002_alter_carrinhoaneis_quantidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrinhoaneis',
            name='quantidade',
            field=models.IntegerField(verbose_name='Quantidade'),
        ),
    ]