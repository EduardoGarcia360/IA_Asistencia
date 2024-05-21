import tkinter as tk
from tkinter import messagebox
import subprocess

def show_main_screen():
    # Limpiar la ventana
    for widget in root.winfo_children():
        widget.destroy()

    # Crear y colocar el botón "Registrar persona"
    register_button = tk.Button(root, text="Registrar persona", command=register_person)
    register_button.pack(pady=10)

    # Crear y colocar el botón "Tomar asistencia"
    attendance_button = tk.Button(root, text="Tomar asistencia", command=take_attendance)
    attendance_button.pack(pady=10)

def register_person():
    # Limpiar la ventana
    for widget in root.winfo_children():
        widget.destroy()

    # Crear y colocar el campo de texto y el botón "Siguiente"
    tk.Label(root, text="Ingrese nombre:").pack(pady=10)
    name_entry = tk.Entry(root)
    name_entry.pack(pady=5)

    def on_next():
        name = name_entry.get()
        if name:
            # Ejecutar el archivo Python capturandoRostros.py con el nombre como argumento
            result = subprocess.run(["python", "capturandoRostros.py", name], check=True)
            if result.returncode == 0:
                # Si capturandoRostros.py se ejecuta correctamente, ejecutar entrenandoRF.py
                subprocess.run(["python", "entrenandoRF.py"], check=True)
                messagebox.showinfo("Registrar persona", f"Nombre ingresado: {name} y entrenamiento completado")
            else:
                messagebox.showerror("Error", "Error al capturar los rostros")
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un nombre")

    # Crear y colocar el botón "Siguiente"
    next_button = tk.Button(root, text="Siguiente", command=on_next)
    next_button.pack(pady=5, side=tk.LEFT, padx=10)
    
    # Crear y colocar el botón "Anterior"
    back_button = tk.Button(root, text="Anterior", command=show_main_screen)
    back_button.pack(pady=5, side=tk.LEFT, padx=10)

def take_attendance():
    #messagebox.showinfo("Tomar asistencia", "Funcionalidad para tomar asistencia")
    subprocess.run(["python", "ReconocimientoFacial.py"], check=True)

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Asistencia")
root.geometry("300x150")

# Mostrar la pantalla principal
show_main_screen()

# Iniciar el bucle principal de la aplicación
root.mainloop()
