from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'nombre',
        'data-sb-validations': 'required'
    }))
    apellido = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'apellido',
        'data-sb-validations': 'required'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'email',
        'data-sb-validations': 'required,email'
    }))


class BuscarForm(forms.Form):
    email = forms.EmailField(label='Email del Cliente', required=True)