# Generated by Django 3.1.1 on 2020-09-17 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carteira', '0002_vendas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendas',
            name='cotacao_atual_venda',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]
