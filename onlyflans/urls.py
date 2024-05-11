"""
URL configuration for onlyflans project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from web.views import * 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("welcome/", welcome, name="welcome"),
    path("contacto_exitoso/", contact_view_exito, name="contacto_exitoso"),
    path("contact_form/", contact_view, name="contact_form"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('flan/<int:flan_id>', flan_details, name='flan_details'),
    
    path('agregar/<int:flan_id>/', agregar_flan, name="Add"),
    path('eliminar/<int:flan_id>/', eliminar_flan, name="Del"),
    path('restar/<int:flan_id>/', restar_flan, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('', tienda, name='tienda'),
    path('filtro/', buscar_flan, name='filtro'),
    
]
