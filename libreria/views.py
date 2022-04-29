from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm


# Create your views here.

def inicio(request):
  return render(request, 'pages/inicio.html')


def nosotros(request):
  return render(request, 'pages/nosotros.html')


def libros(request):
  libros = Libro.objects.all()

  context={
    'libros': libros,
  }

  return render(request, 'libros/index.html', context)

def crear(request):
  formulario = LibroForm(request.POST or None, request.FILES or None)
  if formulario.is_valid():
    formulario.save()
    return redirect('libros')

  context= {
    'formulario': formulario
  }
  return render(request, 'libros/crear.html', context)


def editar(request, id):
  libro = Libro.objects.get(id=id)
  formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)

  if formulario.is_valid() and request.method == 'POST':
    formulario.save()
    return redirect('libros')

  context = {
    'formulario': formulario
  }
  return render(request, 'libros/editar.html', context)


def eliminar(request, id):
  libro = Libro.objects.get(id=id)
  libro.delete()

  return redirect('libros')