from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from pedidos.models import Pedido, LineaPedido
from carro.carro import Carro
from django.contrib import messages
from Store.models import Producto

@login_required(login_url="/autenticacion/logear")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    lineas_pedido = []
    
    for key, value in carro.carro.items():
        producto_id = int(key)
        producto = Producto.objects.get(id=producto_id)
        
        linea_pedido = LineaPedido(
            producto=producto,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido
        )
        linea_pedido.save()
        lineas_pedido.append(linea_pedido)

    messages.success(request, "Has generado el pedido")

    return redirect("Store:store")