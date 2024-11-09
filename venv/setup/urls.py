from django.contrib import admin
from django.urls import path
from iotUbs.views import equipamentos_lista, detalhes_equipamentos
from django.urls import path
#from iotubs.views import equipment_log_list
#from iotUbs.views import TransporteHistoricoView
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('equipamentos/', equipamentos_lista),
    path('equipamentos/<int:pk>', detalhes_equipamentos, name='Detalhes-equipamento'),
    #path('equipment-logs/', views.equipment_log_list, name='equipment_log_list'),
]
