from django.db import models


# Modelo que representa la tabla empleado en MySQL
class Empleado(models.Model):

    # Clave primaria autoincremental
    idEmpleado = models.AutoField(primary_key=True)

    # Nombre del empleado
    nombre = models.CharField(max_length=100)

    # Departamento del empleado
    departamento = models.CharField(max_length=100)

    # Sueldo con 2 decimales
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)

    # Definición del método __str__ para mostrar el nombre y departamento del empleado
    def __str__(self):
        return f"{self.nombre} - {self.departamento}"

    # Nombre exacto de la tabla en MySQL
    class Meta:
        db_table = 'empleado'