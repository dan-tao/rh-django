# generics proporciona vistas genéricas para operaciones comunes como listar, crear, actualizar y eliminar
from rest_framework import generics
from .models import Empleado
from .serializers import EmpleadoSerializer


# GET (listar) y POST (crear)
class EmpleadoListCreateView(generics.ListCreateAPIView):

    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer


# GET por id, PUT y DELETE
class EmpleadoDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

    # Campo utilizado para búsquedas
    lookup_field = 'idEmpleado'