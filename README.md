# Sistema de Inventario en Python

## Descripción

Este programa permite gestionar un inventario básico de productos utilizando Python.
El usuario puede registrar productos, visualizar el inventario actual y calcular estadísticas generales como el valor total almacenado y la cantidad total de unidades.

## Funcionalidades

* Agregar productos al inventario.
* Mostrar todos los productos registrados.
* Calcular estadísticas del inventario.
* Validar datos ingresados por el usuario.
* Menú interactivo en consola.

## Estructura del programa

El sistema utiliza:

* **Lista (`inventario`)** para almacenar todos los productos.
* **Diccionarios** para guardar la información de cada producto:

  * nombre
  * precio
  * cantidad

## Funciones principales

### agregar_producto()

Permite ingresar un nuevo producto validando:

* que el precio sea numérico y positivo
* que la cantidad sea un número entero positivo

### mostrar_inventario()

Muestra todos los productos registrados en pantalla.

### calcular_estadisticas()

Calcula:

* valor total del inventario
* cantidad total de productos almacenados

## Tecnologías usadas

* Python
* Librería `os`
* Librería `time`

## Ejecución

1. Ejecutar el archivo en Python.
2. Seleccionar una opción del menú.
3. Seguir las instrucciones en pantalla.

## Autor

Proyecto realizado por Jefri Calderín.
