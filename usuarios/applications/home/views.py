from django.shortcuts import render

from django.views.generic import (
    TemplateView
)

class HomePage(TemplateView):
    template_name = "home/index.html"

class CasaPage(TemplateView):
    template_name = "home/casa.html"

    