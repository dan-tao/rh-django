from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # Panel admin Django, admin.site.urls es la ruta para acceder al panel admin
    path('admin/', admin.site.urls),

    # API empleados, include permite incluir las urls de la app empleados
    path('api/empleados/', include('empleados.urls')),
]