import pytest
from django.urls import reverse
from Invent_Product.models import Categoria, Producto
import json

@pytest.mark.django_db
def test_index_view(client):
    Categoria.objects.create(nombre_categoria="Electrónica")
    response = client.get(reverse('index'))
    assert response.status_code == 200
    assert "Electrónica" in response.content.decode('utf-8')

@pytest.mark.django_db
def test_productos_por_categoria(client):
    cat = Categoria.objects.create(nombre_categoria="Ropa")
    Producto.objects.create(nombre_producto="Polo", categoria=cat, stock=10, precio=20.0)

    response = client.get(reverse('productos_por_categoria'), {'categoria': 'Ropa'})
    data = response.json()
    assert response.status_code == 200
    assert len(data['products']) == 1
    assert data['products'][0]['nombre_producto'] == "Polo"

@pytest.mark.django_db
def test_buscar_producto(client):
    cat = Categoria.objects.create(nombre_categoria="Accesorios")
    Producto.objects.create(nombre_producto="Reloj", categoria=cat, stock=5, precio=100.0)

    response = client.get(reverse('buscar_producto'), {'nombre': 'Reloj'})
    data = response.json()
    assert response.status_code == 200
    assert data['products'][0]['nombre_producto'] == "Reloj"

@pytest.mark.django_db
def test_agregar_producto(client):
    Categoria.objects.create(nombre_categoria="Videojuegos")

    data = {
        "nombre_producto": "Control Xbox",
        "categoria": "Videojuegos",
        "stock": 12,
        "precio": 299.99
    }
    response = client.post(reverse('agregar_producto'), data=json.dumps(data), content_type="application/json")
    assert response.status_code == 200
    assert response.json()['success'] is True

@pytest.mark.django_db
def test_editar_producto(client):
    cat = Categoria.objects.create(nombre_categoria="Libros")
    producto = Producto.objects.create(nombre_producto="Cien años", categoria=cat, stock=4, precio=50.0)

    nueva_categoria = Categoria.objects.create(nombre_categoria="Literatura")
    data = {
        "nombre_producto": "Cien años de soledad",
        "categoria": "Literatura",
        "stock": 10,
        "precio": 60.0
    }
    response = client.post(reverse('editar_producto', args=[producto.id]), data=json.dumps(data), content_type="application/json")
    assert response.status_code == 200
    assert response.json()['success'] is True

@pytest.mark.django_db
def test_eliminar_producto(client):
    cat = Categoria.objects.create(nombre_categoria="Tecnología")
    producto = Producto.objects.create(nombre_producto="Mouse", categoria=cat, stock=5, precio=25.0)

    response = client.post(reverse('eliminar_producto', args=[producto.id]))
    assert response.status_code == 200
    assert response.json()['success'] is True
