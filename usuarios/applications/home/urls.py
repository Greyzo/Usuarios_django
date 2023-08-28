from django.urls import path
from django.shortcuts import redirect
from . import views

app_name = "home_app"

def redirect_to_panel(request):
    return redirect('home_app:panel')




urlpatterns = [
    path(
        'casa/',
         views.CasaPage.as_view(),
         name = 'casa',
         ),
    path('', 
         redirect_to_panel),
    path('panel/',
         views.HomePage.as_view(),
         name = 'panel',
         ),
]





