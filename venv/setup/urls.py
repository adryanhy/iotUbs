from django.contrib import admin
from django.urls import path
from iotUbs.views import equipamentos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('equipamentos/', equipamentos)
]
