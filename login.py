import mysql.connector #comunicación con una base de datos MySQL
import subprocess
import tkinter as tk  #para crear la interfaz gráfica
from tkinter import messagebox  #para mostrar mensajes emergentes
import chat #las funcionalidades del chatbot
from tkinter import PhotoImage #cargamos img
from PIL import Image, ImageTk, ImageSequence #también imágenes pero con Gifs


# Función para el inicio de sesión
def login():
    global _nom, _con
    try:      #esta se conecta a la base de datos, para buscar si el susuario y contraseña están registrados
        connection = mysql.connector.connect(
            host='localhost',
            database='bd_certus',
            user='root',
            password='' 
        )
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM t_estudiantes WHERE nom_estudiante = '{_nom}'")
        user = cursor.fetchone()
        #si el usuario está registrado en el mysql,podrá acceder en caso contrariio no se habilita nada
        if user is not None and user[3] == _con:
            show_welcome_message()
            return "¡Inicio de sesión exitoso!\n¡Bienvenido!"
        else:
            return "Error en las credenciales"
    except mysql.connector.Error as e:
        return "Error en la consulta: " + str(e)

#este es la ventana emergente que mostrará el mensaje
def show_welcome_message():
    welcome_window = tk.Toplevel()
    welcome_window.title("Bienvenido")
    welcome_label = tk.Label(welcome_window, text="¡Inicio de sesión exitoso!\n¡Bienvenido!", font=("Arial", 12))
    welcome_label.pack()
    close_button = tk.Button(welcome_window, text="Cerrar", command=welcome_window.destroy)
    close_button.pack()
#cuando el usuario le da al boton "iniciar sesión"
def on_login():
    global _nom, _con
    _nom = username_entry.get()
    _con = password_entry.get()
    result = login()
    #el usuario y contraseña deben estar en la base de datos
    if result == "¡Inicio de sesión exitoso!\n¡Bienvenido!":
        chat.open_chat_window(_nom)
    else:
        messagebox.showerror("Error", result)

def register():
    messagebox.showinfo("Bienvenido", "Te vas a registrar a este nuevo mundo:)")
    subprocess.Popen(["python", "crud.py"])


def update_gif_label(frame):
    #Gif
    label.configure(image=frames[frame])
    frame = (frame + 1) % num_frames
    root.after(100, update_gif_label, frame)

#ventana principal-login
root = tk.Tk()
root.title("Inicio de Sesión")

#colores y fuentes de letra
background_color = "#042454"
font = ("Helvetica", 12)
#dimensiones de la ventana
root.geometry("600x480")
root.configure(bg=background_color)

#import archivo GIF
gif_file = Image.open("./sistema-pos-1.gif")
frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif_file)]
num_frames = len(frames)

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

#Label para mostrar el GIF
label = tk.Label(canvas)
label.pack()

#ciclo de actualización para el GIF
update_gif_label(0)      #gIF en bucle.

#image = PhotoImage(file="./EE.png")
#image_label = tk.Label(canvas, image=image, bg=background_color)
#image_label.image = image
#image_label.config(width=400, height=300)
#canvas.create_window(450, 100, anchor="center", window=image_label)

#etiquetas y campos encima de la imagen, con su tipo y color de letra respectivo
username_label = tk.Label(canvas, text="INSTITUTO DE\nEDUCACIÓN SUPERIOR\nTECNOLÓGICO\nPRIVADO CERTUS", font=("Ginebra", 14), bg=background_color, fg="white")
canvas.create_window(367, 15, anchor=tk.NW, window=username_label)

username_label = tk.Label(canvas, text="Usuario:", font=("Helvetica", 14), bg=background_color, fg="white")
canvas.create_window(300, 200, anchor=tk.NW, window=username_label)
username_entry = tk.Entry(canvas, font=("Helvetica", 14))
canvas.create_window(300, 230, anchor=tk.NW, window=username_entry)

password_label = tk.Label(canvas, text="Contraseña:", font=("Helvetica", 14), bg=background_color, fg="white")
canvas.create_window(300, 270, anchor=tk.NW, window=password_label)
password_entry = tk.Entry(canvas, show="*", font=("Helvetica", 14))
canvas.create_window(300, 300, anchor=tk.NW, window=password_entry)


# Botón de inicio de sesión
login_button = tk.Button(canvas, text="Iniciar Sesión", command=on_login, font=("Helvetica", 14), bg="#007BFF", fg="white")
canvas.create_window(300, 350, anchor=tk.NW, window=login_button)

# Botón para registrarse
register_button = tk.Button(canvas, text="Aún no estás registrado?", command=register, font=("Helvetica", 14), bg="#00CC00", fg="white")
canvas.create_window(300, 400, anchor=tk.NW, window=register_button)


root.mainloop()


