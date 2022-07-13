from django import forms
from datetime import date
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



    
class DateInput(forms.DateInput):
    input_type = 'date'

#---------------------------------------------------------------------------------------------------------------------#
 #CLIENTES

class Cliente_formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    fechaVencimiento = forms.DateField(widget=DateInput)
    email = forms.EmailField(max_length=254)
    contraseña = forms.CharField(max_length=30)
    servicio = forms.CharField(max_length=30)
    def clean_servicio(self):
        servicio = self.cleaned_data['servicio']
        if servicio != "NETFLIX" and servicio != "DISNEY" and servicio != "AMAZON":
            raise forms.ValidationError("porfavor ingrese un servicio valido (NETFLIX, DISNEY, AMAZON)")
        return servicio
    def fechaVencimiento_validator(self):
        fechaVencimiento = self.cleaned_data['fechaVencimiento']
        if fechaVencimiento < date.today():
            raise forms.ValidationError("La fecha de vencimiento no puede ser menor a la fecha actual")
        return fechaVencimiento
#---------------------------------------------------------------------------------------------------------------------#
 #EMPLEADOS    
    
class Empleado_formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    area = forms.CharField(max_length=30)
    antiguedad_meses = forms.IntegerField()
    def clean_area(self):
        area = self.cleaned_data['area']
        if area != "ADMINISTRACION" and area != "VENTAS" and area != "DESARROLLO":
            raise forms.ValidationError("porfavor ingrese un area valida 'ADMINISTRACION', 'VENTAS' o 'DESARROLLO'")
        return area
#---------------------------------------------------------------------------------------------------------------------#
 #SERVICIOS
class Servicio_formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=900)
    precio = forms.IntegerField( initial = 0)
    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio < 0:
            raise forms.ValidationError("El precio no puede ser negativo")
        return precio

#---------------------------------------------------------------------------------------------------------------------#
 #REGISTRAR USUARIO
 
 
         
class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El nombre de usuario ya existe')
        return username
    
        
        
    
    
    
    
    class meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_text = {k:"" for k  in fields}
    
    
    
    

    
 #---------------------------------------------------------------------------------------------------------------------#
 #EDITAR USUARIO    
    
    
class UserEditForm(UserCreationForm):
    firt_name = forms.CharField(label='modificar nombre')
    last_name = forms.CharField(label='modificar apellido')
    username = forms.CharField(label='modificar nombre de usuario', required=False)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='modificar Contraseña', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput, required=False)


    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El nombre de usuario ya existe')
        return username
    
    
    class meta:
        model = User
        fields = ['username', 'email','firs_name','last_name' 'password1', 'password2']
        help_text = {k:"" for k  in fields}
