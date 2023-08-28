from django import forms

from .models import User
from django.contrib.auth import authenticate

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )

    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir Contraseña'
            }
        )
    )

    class Meta:
        model = User
        fields = (
                  'username',
                  'email',
                  'identificacion',
                  'nombre',
                  'Pais',
                  'Ciudad',
                  'direccion',
                  'codigoPostal',
                  'NumeroTelefonico',
                      )

        
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no son iguales')


class LoginForm(forms.Form):
     username = forms.CharField(
        label='username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'username',
                'style': '{ margin: 10 px}',
            }
        )
    )
     password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir Contraseña'
            }
        )
    )


     def clean(self):
         clean_data = super(LoginForm,self).clean()
         username = self.cleaned_data['username']
         password = self.cleaned_data['password']

         if not authenticate(username=username, password=password):
             raise forms.ValidationError('los datos de usuario no son correctos')
         return self.cleaned_data
    

     