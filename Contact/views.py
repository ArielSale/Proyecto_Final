from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import EmailMessage
from django.contrib import messages
from .models import Mensaje



def contact(request):
    formulario_contacto = FormularioContacto()
    contexto = {'formulario_contacto': formulario_contacto}

    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            mensaje = request.POST.get("mensaje")

            mensaje_obj = Mensaje(nombre=nombre, email=email, mensaje=mensaje)
            mensaje_obj.save()
            return redirect("Contact:contact_valido")


            # Intento para enviar el formulario por mail
            #email=EmailMessage("Mensaje desde UmamiGastroApp", "El usuario {}, Email {}, Mensaje:\n\n {}".format(nombre,email,mensaje), "", ["tasteoftokyo024@gmail.com"], reply_to=[email])
            #try:
            #    email.send()
            #    return redirect("Contact:contact_valido")  # Redirige a la nueva página contact_valido.html
            
            #except:
            #    return redirect("Contact:contact_no_valido")  # Redirige a la nueva página contact_no_valido.html
                
                

    return render(request, 'Contact/contact.html', contexto )


def contact_valido(request):
    return render(request, 'Contact/contact_valido.html')

def contact_no_valido(request):
    return render(request, 'Contact/contact_no_valido.html')