import mysql.connector
import getpass
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

def insert_data():
    _cod = cod_entry.get()
    _nom = nom_entry.get()
    _ape = ape_entry.get()
    _con = con_entry.get()

    try:
        sql_insert_Query = "INSERT INTO t_estudiantes(cod_estudiante, nom_estudiante, ape_estudiante, con_estudiante) VALUES (%s, %s, %s, %s)"
        cursor = connection.cursor()
        cursor.execute(sql_insert_Query, (_cod, _nom, _ape, _con))
        connection.commit()
        messagebox.showinfo("Éxito", "Registro insertado!")

        cod_entry.delete(0, "end")
        nom_entry.delete(0, "end")
        ape_entry.delete(0, "end")
        con_entry.delete(0, "end")

    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error en la inserción: {e}")

def validate_code(P):
    if len(P) <= 8:
        return True
    else:
        return False

def load_background_image():
    background_image = PhotoImage(file="./certus5.png")
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)  
    background_label.image = background_image

root = tk.Tk()
root.title("Inserción de Datos de Estudiante")
root.geometry("400x300")
load_background_image()

# Colores y fuentes
bg_color = "#F6F7F9"
label_font = ("Helvetica", 12)
entry_font = ("Helvetica", 12)
button_font = ("Helvetica", 12)

# Conexión a la base de datos
try:
    connection = mysql.connector.connect(host='localhost', database='bd_certus', user='root', password='')
except mysql.connector.Error as e:
    messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {e}")
    root.destroy()

# Etiquetas y campos de entrada
cod_label = tk.Label(root, text="Código:", font=label_font, bg=bg_color)
cod_label.pack()
validation = root.register(validate_code) 
cod_entry = tk.Entry(root, validate="key", validatecommand=(validation, "%P"))
cod_entry.pack()

nom_label = tk.Label(root, text="Nombres:", font=label_font, bg=bg_color)
nom_label.pack()
nom_entry = tk.Entry(root)
nom_entry.pack()

ape_label = tk.Label(root, text="Apellidos:", font=label_font, bg=bg_color)
ape_label.pack()
ape_entry = tk.Entry(root)
ape_entry.pack()

con_label = tk.Label(root, text="Contraseña:", font=label_font, bg=bg_color)
con_label.pack()
con_entry = tk.Entry(root, show="*")
con_entry.pack()

insert_button = tk.Button(root, text="Insertar Registro", command=insert_data, font=label_font, bg=bg_color)
insert_button.pack()

root.mainloop()
