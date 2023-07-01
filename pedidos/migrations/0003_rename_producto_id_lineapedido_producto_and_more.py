# Generated by Django 4.2.2 on 2023-06-30 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_rename_pedido_id_lineapedido_pedido_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lineapedido',
            old_name='producto_id',
            new_name='producto',
        ),
        migrations.AlterField(
            model_name='lineapedido',
            name='cantidad',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
