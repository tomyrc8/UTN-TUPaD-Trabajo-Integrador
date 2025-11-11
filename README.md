# Gestor de Paises (Trabajo Integrador)

## Descripcion del programa
Este programa permite gestionar un catalogo de paises utilizando archivos CSV como base de datos.  
El usuario puede agregar, actualizar, buscar, filtrar, ordenar y visualizar estadisticas de los paises almacenados.  
Toda la informacion se guarda de forma persistente en el archivo `integrador.csv`.

## Funcionalidades principales
- **Agregar paises**: Permite registrar nuevos paises con su poblacion, superficie y continente.
- **Actualizar paises**: Modifica datos de poblacion o superficie de un pais existente.
- **Buscar por nombre**: Muestra paises que coinciden total o parcialmente con el nombre ingresado.
- **Filtrar**:
  - Por continente.
  - Por rango de poblacion.
  - Por rango de superficie.
- **Ordenar**:
  - Por nombre (ascendente o descendente).
  - Por poblacion (ascendente o descendente).
  - Por superficie (ascendente o descendente).
- **Mostrar estadisticas**:
  - Pais con mayor y menor poblacion.
  - Promedio de poblacion y superficie.
  - Cantidad de paises por continente.
- **Mostrar todos los paises** en formato tabular.

---

## ⚙️ Instrucciones de uso
1. Ejecutar el archivo Python en la terminal o consola:
   ```bash
   python integrador.py

<img width="543" height="205" alt="image" src="https://github.com/user-attachments/assets/41ad4c3c-4fcd-4e0e-8e9d-77566b9502f8" />

Seguir las instrucciones que aparecen en pantalla.
El programa valida que los campos no esten vacios y que los valores numericos sean correctos.
El archivo integrador.csv se crea automaticamente si no existe.

## Ejemplos de uso
# Ejemplo 1: Agregar un pais

Entrada:

<img width="543" height="315" alt="image" src="https://github.com/user-attachments/assets/413a72c1-e31e-4b0e-99e4-821ada9ecf3f" />


Salida:

<img width="495" height="19" alt="image" src="https://github.com/user-attachments/assets/c407340e-3635-4ced-9e1e-e062daae53de" />

# Ejemplo 2: Buscar un pais
Entrada:

<img width="549" height="259" alt="image" src="https://github.com/user-attachments/assets/7bdf7cc8-4e34-45f1-9b0f-6a05abf52b1c" />

Salida:

<img width="534" height="87" alt="image" src="https://github.com/user-attachments/assets/f7924229-5d94-4313-81f0-aaf61d946a81" />

## Participacion de los integrantes

Juan Manuel Vazquez: desarrollo del codigo, logica de validaciones, manejo de archivos CSV, estructura de menus y estadisticas.

Tomas Jabbur: desarrollo del codigo, implementacion de funciones de filtrado, ordenamiento y busqueda, ademas de las pruebas y ajustes finales del programa.

## Diagrama de flujo de funciones principales

<img width="1134" height="660" alt="image" src="https://github.com/user-attachments/assets/9a97c1b7-d396-4d23-9046-cb3064c2d975" />


