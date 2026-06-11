from django.urls import path
from .views import (
    EmpleadoListCreateView,
    EmpleadoDetailView
)

urlpatterns = [

    # Listar y crear empleados
    path(
        '',
        EmpleadoListCreateView.as_view(),
        name='empleado-list-create'
    ),

    # Buscar, editar y eliminar, empleadodetailview se encarga de las operaciones por id, asview convierte la clase en una vista
    path(
        '<int:idEmpleado>/',
        EmpleadoDetailView.as_view(),
        name='empleado-detail'
    ),
]