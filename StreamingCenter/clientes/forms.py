from django import forms

class NetflixFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    
    