import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

def insert_data():
    _cod = entries["Código"].get()
    _nom = entries["Nombres"].get()
    _ape = entries["Apellidos"].get()
    _con = entries["Contraseña"].get()

    try:
        sql_insert_Query = "INSERT INTO t_estudiantes(cod_estudiante, nom_estudiante, ape_estudiante, con_estudiante) VALUES (%s, %s, %s, %s)"
        cursor = connection.cursor()
        cursor.execute(sql_insert_Query, (_cod, _nom, _ape, _con))
        connection.commit()
        messagebox.showinfo("Éxito", "Registro insertado!")

        clear_entries()

    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error en la inserción: {e}")

def validate_code(P):
    return len(P) <= 8

def load_background_image():
    background_image = PhotoImage(file="tt2.png")
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)
    background_label.image = background_image

def clear_entries():
    for entry in entries.values():
        entry.delete(0, "end")

root = tk.Tk()
root.title("Inserción de Datos de Estudiante")
root.geometry("400x300")
root.configure(bg="#F6F7F9")
load_background_image()

# Conexión a la base de datos
try:
    connection = mysql.connector.connect(host='localhost', database='bd_certus', user='root', password='')
except mysql.connector.Error as e:
    messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {e}")
    root.destroy()

# Etiquetas y campos de entrada
label_font = ("Helvetica", 14)
bg_color = "#F6F7F9"

fields = ["Código", "Nombres", "Apellidos", "Contraseña"]
entries = {}

for i, field in enumerate(fields, start=1):
    label = tk.Label(root, text=f"{field}:", font=label_font, bg=bg_color)
    label.place(x=50, y=30 + i * 40)

    entry = tk.Entry(root, show="*" if field == "Contraseña" else "", font=label_font, width=15)
    entry.place(x=200, y=30 + i * 40)
    entries[field] = entry

insert_button = tk.Button(root, text="Insertar Registro", command=insert_data, font=label_font, bg=bg_color)
insert_button.place(x=200, y=230)

root.mainloop()
