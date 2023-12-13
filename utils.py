import mysql.connector

def store_user_interaction(username, user_message, bot_response):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='bd_certus',
            user='root',
            password=''
        )

        cursor = connection.cursor()

        query = "INSERT INTO t_interacciones_chatbot (usuario, mensaje_usuario, respuesta_bot) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, user_message, bot_response))

        connection.commit()

    except mysql.connector.Error as e:
        print(f"Error al almacenar interacción en la base de datos: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
