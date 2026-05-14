# logica.py
from deque import MiDeque

class ActionManager:
    def __init__(self):
        self.historial = MiDeque() # Aqui guardamos las acciones normales
        self.rehacer_stack = MiDeque() # Aqui lo que quitamos con Undo
        self.estado_actual = "Inicio"

    def nueva_accion(self, accion):
        if accion.strip() == "":
            return False # Validacion simple para no agregar vacios
        
        self.historial.add_rear(accion)
        self.estado_actual = accion
        # Si hacemos una accion nueva, el redo se debe limpiar
        self.rehacer_stack = MiDeque() 
        return True

    def undo(self):
        if self.historial.is_empty():
            print("No hay nada que deshacer")
            return None
        
        # Sacamos el ultimo y lo mandamos a la otra lista
        accion = self.historial.remove_rear()
        self.rehacer_stack.add_front(accion)
        
        # Actualizamos el estado actual al que quedo de ultimo
        if self.historial.is_empty():
            self.estado_actual = "Inicio"
        else:
            lista = self.historial.obtener_lista()
            self.estado_actual = lista[-1]
        return accion

    def redo(self):
        if self.rehacer_stack.is_empty():
            print("No hay nada que rehacer")
            return None
        
        # Sacamos de rehacer y devolvemos al historial
        accion = self.rehacer_stack.remove_front()
        self.historial.add_rear(accion)
        self.estado_actual = accion
        return accion

    def mostrar_historial(self):
        return self.historial.obtener_lista()