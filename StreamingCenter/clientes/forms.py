from django import forms

class Cliente_formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    fechaVencimiento = forms.DateField()
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
    
class Servicio_formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=200)
    precio = forms.IntegerField()
    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio < 0:
            raise forms.ValidationError("El precio no puede ser negativo")
        return precio

        
    