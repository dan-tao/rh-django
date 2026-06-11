from rest_framework import serializers
from .models import Empleado


# Serializer del modelo Empleado
class EmpleadoSerializer(serializers.ModelSerializer):

    # Meta class para definir el modelo y los campos a exponer
    class Meta:
        model = Empleado

        # Campos que serán expuestos en el API
        fields = '__all__'

    # Validación del nombre, self hace referencia al campo que se está validando
    def validate_nombre(self, value):

        if len(value.strip()) < 2:
            raise serializers.ValidationError(
                "El nombre debe tener mínimo 2 caracteres."
            )

        return value

    # Validación del departamento
    def validate_departamento(self, value):

        if len(value.strip()) < 2:
            raise serializers.ValidationError(
                "El departamento debe tener mínimo 2 caracteres."
            )

        return value

    # Validación del sueldo
    def validate_sueldo(self, value):

        if value <= 0:
            raise serializers.ValidationError(
                "El sueldo debe ser mayor que cero."
            )

        return value