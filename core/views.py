from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Marca, Suscripcion, Membresia, Envio
from .forms import ContactoForm, ProductoForm, CustomUserCreationForm, SuscripcionForm, EnvioForm, EnvioForm1
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import ProductoSerializer, MarcaSerializer, SuscripcionSerializer, MembresiaSerializer
#------
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
#------
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class NombrememViewset(viewsets.ModelViewSet):
    queryset = Membresia.objects.all()
    serializer_class = MembresiaSerializer

class MarcaViewset(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_queryset(self):
        productos = Producto.objects.all()
        nombre = self.request.GET.get('nombre')

        if nombre:
            productos = productos.filter(nombre__contains=nombre)
        return productos

class SuscripcionViewset(viewsets.ModelViewSet):
    queryset = Suscripcion.objects.all()
    serializer_class = SuscripcionSerializer


def index(request):
    productos = Producto.objects.all()
    data= {
        'productos': productos
    }
    return render(request, 'core/index.html', data)

def admindj(request):

    return render(request, 'core/admindj.html')

def contactanos(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario

    return render(request, 'core/contactanos.html', data)

def registro(request):

    return render(request, 'core/registro.html')

@permission_required('core.add_producto')
def agregar_producto(request):

    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Ingresado")
        else:
            data["form"] = formulario

    return render(request, 'core/admindj.html', data)

@permission_required('core.view_producto')
def listar_productos(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        'productos': productos,
        'paginator': paginator
    }

    return render(request, 'core/listar.html', data)

@permission_required('core.change_producto')
def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    data ={
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificado correctamente")
            return redirect(to='listar_productos')
        data["form"] = formulario

    return render(request, 'core/modificar.html', data)

@permission_required('core.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "eliminado correctamente")
    return redirect(to="listar_productos")


def registro1(request):

    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado")
            return redirect(to="index")
        data["form"] = formulario

    return render(request, 'registration/registro1.html', data)


def carrito(request):
    return render(request, 'core/carrito.html')


def agregar_membresia(request):
    data = {
        'form': SuscripcionForm()
    }
    if request.method == 'POST':
        formulario = SuscripcionForm(data = request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Membresia Agregada Correctamente")
            return redirect(to = "index")
        else:
            data["form"] = formulario
    return render(request, 'suscripcion/sub.html',data)

def listar_membresia(request):
    suscripciones = Suscripcion.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(suscripciones, 7)
        suscripciones = paginator.page(page)
    except:
        raise Http404
    
    
    data = {
        'sub': suscripciones,
        'paginator' : paginator
    }
    return render(request, 'suscripcion/listarsub.html', data)

def eliminar_membresia(request, id):
    suscripcion = get_object_or_404(Suscripcion, id = id)
    suscripcion.delete()
    messages.success(request, "Membresia Eliminada  Correctamente")
    return redirect(to = "listar_membresia")

@login_required
def agregar_envio(request):
    data= {
        'form' : EnvioForm()
    }
    if request.method == 'POST':
        formulario = EnvioForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Compra realizada")
            return redirect(to = "index")
        else:
            data["form"] = formulario

    return render(request, 'envio/agregar.html',data)


def listar_envio(request):
    envio = Envio.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(envio, 5)
        envio = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': envio,
        'paginator': paginator
    }
    return render(request, 'envio/listar.html',data)


@login_required
def listar_envio_usuario(request):
    envio = Envio.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(envio, 5)
        envio = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': envio,
        'paginator': paginator
    }
    return render(request, 'core/historial.html',data)


@login_required
def modificar_envio(request ,  id):
    envio = get_object_or_404(Envio, id = id)
    data = {
        'form': EnvioForm1(instance=envio)
    }

    if request.method == 'POST':
        formulario = EnvioForm1(data=request.POST, instance=envio, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listar_envio")
        data["form"]=formulario

    return render(request, 'envio/modificar.html',data)