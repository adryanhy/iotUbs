from django.contrib import admin
from django.urls import path
from iotUbs.views import equipamentos_lista, detalhes_equipamentos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('equipamentos/', equipamentos_lista),
    path('equipamentos/<int:pk>', detalhes_equipamentos, name='Detalhes-equipamento'),
]
