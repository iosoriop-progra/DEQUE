Sistema de Edición con Estructura Deque (Undo/Redo)

Este proyecto es un Editor de Acciones desarrollado en Python que implementa una estructura de datos Deque (Double-Ended Queue) personalizada para gestionar un sistema de Deshacer (Undo) y Rehacer (Redo).

El diseño visual está inspirado en un bloc de notas moderno, utilizando una interfaz gráfica con colores pastel y una distribución lateral para una mejor experiencia de usuario.

/////

Características:

Registro de Acciones: Permite ingresar y almacenar texto de forma cronológica.

Sistema Undo/Redo: Navegación fluida por el historial de cambios utilizando una doble estructura de datos.

Historial Dinámico: Visualización en tiempo real de todas las acciones almacenadas.

Interfaz Pastel: UI moderna construida con CustomTkinter con bordes redondeados y tipografía clara.

Validaciones Robustas: Manejo de entradas vacías y estados de historial vacío.

//////

Librería de UI: CustomTkinter

Estructura de Datos: Deque personalizada (implementada manualmente sin librerías externas).

Estructura del Proyecto
deque.py: Contiene la implementación de la clase MiDeque con sus métodos fundamentales (add_front, add_rear, remove_front, remove_rear, is_empty, size).

logica.py: Contiene la clase ActionManager, que encapsula la lógica del negocio y la gestión de los estados de Undo y Redo.

main.py: Punto de entrada de la aplicación y definición de la interfaz gráfica (AppEditor).

////

Instalación y Ejecución
Clonar el repositorio o descargar los archivos.

Instalar dependencias:
pip install customtkinter

Ejecutar la aplicación:
python main.py

/////

Lógica de la Deque 
La estructura Deque fue elegida por su versatilidad para insertar y eliminar elementos por ambos extremos. En este sistema:

Undo: Se elimina el último elemento del historial (remove_rear) y se inserta al frente del stack de rehacer (add_front).

Redo: Se elimina del frente del stack de rehacer (remove_front) y se devuelve al final del historial (add_rear).
