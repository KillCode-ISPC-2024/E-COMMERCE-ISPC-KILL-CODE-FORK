# Generated by Django 4.2.1 on 2023-06-20 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databaseManager', '0007_alter_pedido_idpedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='idPedido',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]