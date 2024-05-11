from django.shortcuts import get_object_or_404, redirect, render
from web.models import Flan
from .forms import ContactForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from web.Carrito import Carrito
from django.db.models import Q




# Create your views here.


def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request , 'index.html',{'flanes': flanes_publicos})

def about(request):
    return render(request, 'about.html', {})

@login_required 
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'flanes': flanes_privados})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto_exitoso')
    else:
        form = ContactForm()
    return render(request,'contact_form.html',{'form': form })


def contact_view_exito(request):
    return render(request , 'contacto_exitoso.html',{})

class Customloginview(LoginView):
    template_name = 'registration/login.html'
    
class CustomLogoutView(LogoutView):
    next_page = "/"
    


def flan_details(request ,flan_id):
    flan = get_object_or_404(Flan,pk=flan_id)
    return render(request, 'flan_details.html',{'flan':flan})
    
###CARRITO DE COMPRAS### 

def tienda(request, template_name='index.html'):
    flan = Flan.objects.all()
    return render(request, template_name, {'flan':flan})

#def flan_details(request):
#    return tienda(request, template_name='flan_details.html')

#def tienda(request):
#    flan = flan.objects.all()
#    return render(request, "index.html", {'flan':flan})

def agregar_flan(request, flan_id):
    carrito = Carrito(request)
    flan = Flan.objects.get(id=flan_id)
    carrito.agregar(flan)
    return redirect("tienda")

def eliminar_flan(request, flan_id):
    carrito = Carrito(request)
    flan = Flan.objects.get(id=flan_id)
    carrito.eliminar(flan)
    return redirect("tienda")

def restar_flan(request, flan_id):
    carrito = Carrito(request)
    flan = Flan.objects.get(id=flan_id)
    carrito.restar(flan)
    return redirect("tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("tienda")

# BUSCADOR

def buscar_flan(request):
    criterio = request.GET.get("papita")
    flanes = Flan.objects.all()
    if not request.user.is_authenticated:
        flanes = Flan.objects.filter(is_private = False)
        
    if criterio: 
        flanes = flanes.filter(
            Q(name__icontains=criterio)| Q(descripcion__icontains=criterio)
        )
    return render(request,'index.html',{"flanes":flanes})