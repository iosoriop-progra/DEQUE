import customtkinter as ctk
from tkinter import messagebox
from deque import MiDeque 

class ActionManager:
    def __init__(self):
        self.historial = MiDeque()
        self.rehacer_stack = MiDeque()
        self.estado_actual = "Sin acciones"

    def registrar_accion(self, texto):
        if not texto.strip(): return False
        self.historial.add_rear(texto)
        self.estado_actual = texto
        self.rehacer_stack = MiDeque() 
        return True

    def undo(self):
        if self.historial.is_empty(): return None
        accion = self.historial.remove_rear()
        self.rehacer_stack.add_front(accion)
        if self.historial.is_empty():
            self.estado_actual = "Inicio"
        else:
            acciones = self.historial.get_all()
            self.estado_actual = acciones[-1]
        return accion

    def redo(self):
        if self.rehacer_stack.is_empty(): return None
        accion = self.rehacer_stack.remove_front()
        self.historial.add_rear(accion)
        self.estado_actual = accion
        return accion


class AppEditor(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.manager = ActionManager()

        
        self.title(" Estructura Deque")
        self.geometry("900x600") 
        ctk.set_appearance_mode("light")
        
        self.font_titulo = ("Arial Rounded MT Bold", 26)
        self.font_botones = ("Segoe UI", 14, "bold")

        
        self.main_frame = ctk.CTkFrame(self, fg_color="#A7CDF3", corner_radius=20)
        self.main_frame.pack(padx=15, pady=15, fill="both", expand=True)

        
        self.header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.header_frame.pack(pady=20, fill="x")

        self.label_titulo = ctk.CTkLabel(self.header_frame, text="Editor con Deque Personalizada", font=self.font_titulo, text_color="#2216D3")
        self.label_titulo.pack()

        
        self.input_row = ctk.CTkFrame(self.header_frame, fg_color="transparent")
        self.input_row.pack(pady=15)

        self.entry_accion = ctk.CTkEntry(self.input_row, placeholder_text="Escribe aquí tu nueva acción...", 
                                        width=500, height=45, corner_radius=15, border_color="#FAF62C")
        self.entry_accion.pack(side="left", padx=10)

        self.btn_add = ctk.CTkButton(self.input_row, text="Registrar", command=self.agregar, 
                                     fg_color="#1DD41D", text_color="#0D0E07", hover_color="#C2D3C2", 
                                     height=45, width=120, corner_radius=15, font=self.font_botones)
        self.btn_add.pack(side="left")

        
        self.body_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.body_frame.pack(padx=20, pady=10, fill="both", expand=True)

        
        self.left_sidebar = ctk.CTkFrame(self.body_frame, fg_color="#F0F4F8", corner_radius=20, width=180)
        self.left_sidebar.pack(side="left", fill="y", padx=(0, 15))

        ctk.CTkLabel(self.left_sidebar, text="CONTROLES", font=("Segoe UI", 12, "bold"), text_color="gray").pack(pady=(20, 10))

        self.btn_undo = ctk.CTkButton(self.left_sidebar, text="⟲ Undo", width=140, height=60, command=self.deshacer,
                                      fg_color="#EECD8B", text_color="#B17C0A", hover_color="#EECD8B", corner_radius=15, font=self.font_botones)
        self.btn_undo.pack(pady=10, padx=20)

        self.btn_redo = ctk.CTkButton(self.left_sidebar, text="Redo ⟳", width=140, height=60, command=self.rehacer,
                                      fg_color="#71DDCB", text_color="#078F76", hover_color="#98E9DB", corner_radius=15, font=self.font_botones)
        self.btn_redo.pack(pady=10, padx=20)

        
        self.center_panel = ctk.CTkFrame(self.body_frame, fg_color="#F0F4F8", corner_radius=20)
        self.center_panel.pack(side="left", fill="both", expand=True)

        self.label_estado = ctk.CTkLabel(self.center_panel, text="Estado Actual: Inicio", font=("Segoe UI", 18, "bold"), text_color="#020300")
        self.label_estado.pack(pady=(15, 5))

        self.txt_historial = ctk.CTkTextbox(self.center_panel, corner_radius=15, border_width=2, 
                                            border_color="#FFFFFF", fg_color="white", text_color="#333", font=("Consolas", 15))
        self.txt_historial.pack(pady=15, padx=20, fill="both", expand=True)
        self.txt_historial.configure(state="disabled")

    def actualizar_interfaz(self):
        self.label_estado.configure(text=f"Estado Actual: {self.manager.estado_actual}")
        self.txt_historial.configure(state="normal")
        self.txt_historial.delete("1.0", "end")
        acciones = self.manager.historial.get_all()
        for i, acc in enumerate(acciones, 1):
            self.txt_historial.insert("end", f" Accion #{i}: {acc}\n")
        self.txt_historial.configure(state="disabled")

    def agregar(self):
        texto = self.entry_accion.get()
        if self.manager.registrar_accion(texto):
            self.entry_accion.delete(0, "end")
            self.actualizar_interfaz()
        else:
            messagebox.showwarning("Campo Vacío", "Por favor, escribe una acción para registrar.")

    def deshacer(self):
        if not self.manager.undo():
            messagebox.showinfo("Información", "No hay acciones previas en el historial.")
        self.actualizar_interfaz()

    def rehacer(self):
        if not self.manager.redo():
            messagebox.showinfo("Información", "No hay nada que rehacer en este momento.")
        self.actualizar_interfaz()

if __name__ == "__main__":
    app = AppEditor()
    app.mainloop()