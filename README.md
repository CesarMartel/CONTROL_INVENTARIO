🛒 Proyecto Mini CRUD: Inventario de Productos
📌 Descripción del Proyecto
Este proyecto es una aplicación web de inventario de productos desarrollada con 

Django que permite a los usuarios gestionar un catálogo de productos a través de operaciones CRUD (Crear, Leer, Actualizar, Borrar). El objetivo principal del proyecto fue aplicar las metodologías ágiles 



Scrum y Extreme Programming (XP), utilizando GitHub para la colaboración y configurando la Integración Continua (CI) con GitHub Actions.


El sistema busca brindar una interfaz intuitiva y eficiente que facilite la administración y visualización de productos.

🔧 Funcionalidades Principales

Registro de Productos: Los usuarios pueden agregar nuevos productos, especificando el nombre, la categoría, el precio y el stock.



Visualización de Productos: Los productos registrados se muestran en una tabla dinámica para su fácil consulta.


Actualización de Productos: Los usuarios pueden editar la información de productos existentes.


Eliminación de Productos: El sistema permite borrar productos del inventario.

👥 Integrantes y Roles del Equipo
Rol	Nombre
Scrum Master	
César Martel 

Developer Backend	
Miguel Ruiz y Sebastian Rosas 

Developer Frontend	
Yhefritd Huacho y Fernando Dionicio 

✅ Historias de Usuario Principales

CRUD de Productos: Como usuario, necesito registrar, ver, actualizar y eliminar productos en un inventario, especificando el producto, categoría, precio y stock.


Estado: ✅ Completado


Interfaz de Usuario: Como usuario, necesito que la aplicación tenga una interfaz clara y fácil de usar para interactuar con el inventario.

Estado: ✅ Completado

🛠️ Instalación del Proyecto
Requisitos
Python 3.10 o superior

Django 4.x

Git

Pasos de Instalación
Clona el repositorio:

Bash

git clone https://github.com/CesarMartel/CONTROL_INVENTARIO.git
cd CONTROL_INVENTARIO
Crea y activa un entorno virtual:

Bash

python -m venv .env
# En Linux/Mac
source .env/bin/activate
# En Windows
.env\Scripts\activate
Instala las dependencias:

Bash

pip install -r requirements.txt
Aplica las migraciones de la base de datos:

Bash

python manage.py migrate
Ejecuta el servidor de desarrollo:

Bash

python manage.py runserver
🗂️ Estructura del Tablero Trello
El equipo utiliza 

Trello para organizar el flujo de trabajo de acuerdo con la metodología Scrum + XP. El tablero incluye columnas como "Product Backlog", "Sprint Planning", "Sprint Backlog", "In Progress", "Review" y "Done". Cada tarea incluye etiquetas por prioridad, asignación a un miembro del equipo y un checklist de seguimiento.

🔗 Accesos Directos
Tablero Trello: 👉🔗 [https://trello.com/invite/b/689101684d151b9cd01d7b26/ATTI2b9c5650f823ab949fb68f231a90528dF092CE8E/controlinventario]

Repositorio GitHub: 👉🔗 [https://github.com/CesarMartel/CONTROL_INVENTARIO.git]

