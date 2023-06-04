from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .models import Empleado, ObraSocial, Art, Extra, Deduccion, Recibo


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8)

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password')


    def validate_password(self, value):
        return make_password(value)


class CrearEmpleadoSerializer(serializers.ModelSerializer):
    legajo = serializers.IntegerField()
    nombre = serializers.CharField(max_length=200)
    apellido = serializers.CharField(max_length=200)
    calle = serializers.CharField(max_length=200)
    casa_piso_numero = serializers.IntegerField()
    provincia = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    telefono = serializers.IntegerField()
    cargo = serializers.CharField(max_length=200)
    categoria = serializers.CharField(max_length=200)
    fecha_ingreso = serializers.DateField()
    fecha_nacimiento = serializers.DateField()
    ciudad = serializers.CharField(max_length=200)
    cuil_empleado = serializers.IntegerField()
    obra_social = serializers.SlugRelatedField(slug_field='id_ObraSocial', queryset=ObraSocial.objects.all())
    art = serializers.SlugRelatedField(slug_field='id_art', queryset=Art.objects.all())

    class Meta:
        model = Empleado
        fields = '__all__'

class CrearReciboSerializer(serializers.ModelSerializer):
    id_recibo = serializers.IntegerField()
    montoBruto = serializers.DecimalField(max_digits=8, decimal_places=2)
    montoNeto = serializers.DecimalField(max_digits=8, decimal_places=2)
    periodo = serializers.DateField()
    antiguedad = serializers.IntegerField()
    concepto = serializers.CharField(max_length=200)
    asistencia = serializers.DecimalField(max_digits=8, decimal_places=2)
    fecha_pago = serializers.DateField()
    deduccion = serializers.SlugRelatedField(
        slug_field='cod_deduccion', queryset=Deduccion.objects.all())
    extra = serializers.SlugRelatedField(
        slug_field='cod_extra', queryset=Extra.objects.all())
    legajo_empleado = serializers.SlugRelatedField(
        slug_field='legajo', queryset=Empleado.objects.all())
    
    class Meta:
        model = Recibo
        fields = '__all__'
