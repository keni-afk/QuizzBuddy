import tkinter as tk
from tkinter import scrolledtext
import mysql.connector

#va abrir la ventana de chat
def open_chat_window(username):
    chat_window = tk.Toplevel() #venatana emergente
    chat_window.title("Chat-Bot") #titulo de la ventana
    chat_window.configure(bg="#E6E6E6")
    chat_window.geometry("400x440")  #dimensiones de la ventana

#cuando el user da click en enviar su mensaje
    def send_message():
        user_input = user_message.get()
        display_message("Tú: " + user_input, "#E6E6E6")
        handle_user_message(user_input) #mostramos el mensaje en el chat
        user_message.delete(0, tk.END)
    #muestra el mensaje en el chat, config su fondo
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

    #mnsjs del user
    def handle_user_message(user_input):
        cleaned_input = user_input.lower().strip()

        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='bd_certus',
                user='root',
                password=''
            )

            cursor = connection.cursor()

            query = "SELECT respuesta FROM t_respuestas_chatbot WHERE pregunta = %s"
            cursor.execute(query, (cleaned_input,))
            result = cursor.fetchone()

            if result:
                response = result[0]
                display_message("Bot: " + response)
            else:
                display_message("Bot: No estoy seguro de lo que quieres, disculpa, ¿puedes intentarlo de nuevo?")

        except mysql.connector.Error as e:
            display_message("Bot: Ocurrió un error al procesar tu solicitud. Por favor, inténtalo de nuevo más tarde.")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    display_message(f"Bot: ¡Bienvenido al chat, {username}! ¿En qué puedo ayudarte?")
    chat_window.mainloop()

if __name__ == "__main__":
    open_chat_window()

