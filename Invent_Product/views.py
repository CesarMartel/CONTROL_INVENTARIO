from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Categoria, Producto
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

# Página principal: muestra todas las categorías
def index(request):
    categorias = Categoria.objects.all()
    return render(request, 'index.html', {'categorias': categorias})

# Obtener productos por nombre de categoría
def productos_por_categoria(request):
    categoria_nombre = request.GET.get('categoria')
    productos = Producto.objects.filter(categoria__nombre_categoria=categoria_nombre)
    
    product_data = [
        {
            'id': p.id,
            'nombre_producto': p.nombre_producto,
            'precio': float(p.precio),
            'stock': p.stock,
            'categoria': p.categoria.nombre_categoria
        }
        for p in productos
    ]
    return JsonResponse({'products': product_data})

# Buscar productos por nombre (filtro parcial)
def buscar_producto(request):
    nombre = request.GET.get('nombre', '')
    productos = Producto.objects.filter(nombre_producto__icontains=nombre)

    product_data = [
        {
            'id': p.id,
            'nombre_producto': p.nombre_producto,
            'precio': float(p.precio),
            'stock': p.stock,
            'categoria': p.categoria.nombre_categoria
        }
        for p in productos
    ]
    return JsonResponse({'products': product_data})

# Agregar nuevo producto
@csrf_exempt
@require_http_methods(["POST"])
def agregar_producto(request):
    try:
        data = json.loads(request.body)
        nombre = data.get('nombre_producto')
        categoria_nombre = data.get('categoria')
        stock = int(data.get('stock', 0))
        precio = float(data.get('precio', 0.0))

        categoria = get_object_or_404(Categoria, nombre_categoria=categoria_nombre)

        producto = Producto.objects.create(
            nombre_producto=nombre,
            categoria=categoria,
            stock=stock,
            precio=precio
        )

        return JsonResponse({'success': True, 'id': producto.id})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

# Editar un producto existente
@csrf_exempt
@require_http_methods(["POST", "PUT"])
def editar_producto(request, producto_id):
    try:
        data = json.loads(request.body)
        nombre = data.get('nombre_producto')
        categoria_nombre = data.get('categoria')
        stock = int(data.get('stock', 0))
        precio = float(data.get('precio', 0.0))

        producto = get_object_or_404(Producto, id=producto_id)
        categoria = get_object_or_404(Categoria, nombre_categoria=categoria_nombre)

        producto.nombre_producto = nombre
        producto.categoria = categoria
        producto.stock = stock
        producto.precio = precio
        producto.save()

        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

# Eliminar un producto
@csrf_exempt
@require_http_methods(["POST"])
def eliminar_producto(request, producto_id):
    try:
        producto = get_object_or_404(Producto, id=producto_id)
        producto.delete()
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})
