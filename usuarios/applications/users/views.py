from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from applications.home import views


from django.views.generic import (
    CreateView,
    View
)

from django.views.generic.edit import (
    FormView
)

from .forms import UserRegisterForm, LoginForm
from .models import User

class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self, form):
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            identificacion=form.cleaned_data['identificacion'],
            nombre=form.cleaned_data['nombre'],
            Pais=form.cleaned_data['Pais'],
            Ciudad=form.cleaned_data['Ciudad'],
            direccion=form.cleaned_data['direccion'],
            codigoPostal=form.cleaned_data['codigoPostal'],
            NumeroTelefonico=form.cleaned_data['NumeroTelefonico'],
        )
        return super(UserRegisterView, self).form_valid(form)

    

class LoginUser(FormView):
    template_name= 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:casa')

    def form_valid(self, form):
         user = authenticate(
             username=form.cleaned_data['username'],
             password=form.cleaned_data['password'],
         )
         login(self.request, user)
         return super(LoginUser, self).form_valid(form)
    

class LogoutView(View):
    def get(self,request,*args,**kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
            'home_app:panel'
            #'users_app:user-login'
            )
        )