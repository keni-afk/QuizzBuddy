import tkinter as tk
from tkinter import scrolledtext
import time  

def open_chat_window(username):
    chat_window = tk.Toplevel()
    chat_window.title("Chat-Bot")#titulo de la ventana
    chat_window.configure(bg="#E6E6E6")
    chat_window.geometry("400x440")  #dimensiones de la ventana


    def send_message():
        user_input = user_message.get()
        display_message("Tú: " + user_input, "#E6E6E6")
        handle_user_message(user_input)
        user_message.delete(0, tk.END)

    def display_message(message, background_color="white"):
        chat_display.insert(tk.END, message + "\n")
        chat_display.see(tk.END)
        chat_display.tag_configure("custom", background=background_color)
        chat_display.tag_add("custom", chat_display.index(tk.INSERT))

    chat_display = scrolledtext.ScrolledText(chat_window, width=50, height=20, font=("Arial", 12))
    chat_display.configure(bg="white")
    chat_display.pack()

    user_message = tk.Entry(chat_window, width=40, font=("Arial", 12))
    user_message.configure(bg="white")
    user_message.pack()

    send_button = tk.Button(chat_window, text="Enviar", command=send_message, font=("Arial", 12))
    send_button.configure(bg="#007BFF", fg="white")
    send_button.pack()

    def handle_user_message(user_input):
        
        cleaned_input = user_input.lower().strip()
        
        keyword_responses = {
            'hola': 'Hola soy botCertus 😊 ¿En qué puedo ayudarte?',
            'información básica curso': 'La Unidad Didáctica Integradora "Diseño de\nSoluciones de Inteligencia Artificial"\ncorresponde a la carrera de Diseño y Desarrollo\nde Software y Soluciones Móviles y tiene carácter\nteórico-práctico.\nA través de ella se busca que el estudiante sea\ncapaz de diseñar soluciones de inteligencia\nartificial utilizando diferentes servicios y\nherramientas de Machine Learning.',
            'requisitos curso': 'Los requisitos del curso incluyen:\n1.Previo saberes de implemnetación\n2.Puntulidad de acuerdo a los horarios',
            'grabaciones de las clases': 'Puedes ver las grabaciones de las clases en las siguientes fechas:\nVer Grabación = miércoles, 11 de octubre de 2023.\nVer Grabación = miércoles, 04 de octubre de 2023\nVer Grabación = miércoles, 04 de octubre de 2023.\nVer Grabación = miércoles, 04 de octubre de 2023.\nVer Grabación = miércoles, 04 de octubre de 2023.\nVer Grabación = miércoles, 04 de octubre de 2023.',
            'sistemas de evaluación': 'La calificación de las evidencias 3 y 4 (E3 y E4)\nse obtiene al aplicar la siguiente fórmula:\nE3 = PF3(0.70) + PA(0.30),\nE4 = PF4(0.70) + C(0.30).\nFinalmente, para la calificación final (CF)\nde la unidad didáctica se aplica\nla siguiente fórmula:\nCF = E1(0.15) + E2(0.20) + E3(0.30) + E4(0.35).',
            'dudas sobre el contenido del curso': 'El desarrollo de la unidad didáctica es fundamental porque\npermitirá al estudiante identificar problemas\nque pueden ser abordados mediante el\nuso de inteligencia artificial,\n y aplicar técnicas de análisis de datos y\naprendizaje automático para diseñar soluciones efectivas.\n Así como evaluar modelos de inteligencia\nartificial, utilizando herramientas y plataformas comunes,e interpretar los resultados\npara asegurar la precisión y la efectividad del modelo.'
        }

        response = None
        for keyword, reply in keyword_responses.items():
            if keyword in cleaned_input:
                response = reply
                break
        if response:
            display_message("Bot: " + response)
        else:
            display_message("Bot: 'No estoy seguro de lo quieres, disculpa, puedes intentarlo de nuevo?")

        #si el usuario demora en responder 30seg enviará este mensaje
    def simulate_bot_response():
        time.sleep(30)
        display_message("Bot: Estoy aquí para ayudarte. Qué necesitas?")
    #será un chat personalizado ya que el nombre ingresado en el loginserá parte de la bienvenida
    display_message(f"Bot: ¡Bienvenido al chat, {username}! ¿En qué puedo ayudarte?")
    chat_window.after(1000, simulate_bot_response) 

    chat_window.mainloop()

if __name__ == "__main__":
    open_chat_window()

