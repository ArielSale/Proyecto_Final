from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('UmamiGastroApp/', include('UmamiGastroApp.urls', namespace='UmamiGastroApp')),
    path('Contact/', include('Contact.urls', namespace='Contact')),
    path('Store/', include('Store.urls', namespace='Store')),
    path('News/', include('News.urls', namespace='News')),
    path('carro/', include('carro.urls', namespace='carro')),
    path('autenticacion/', include('autenticacion.urls', namespace='autenticacion')),
    path('pedidos/', include('pedidos.urls', namespace='pedidos'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [path('media/<path>', serve, {'document_root': settings.MEDIA_ROOT})]