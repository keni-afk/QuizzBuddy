import mysql.connector
import getpass
import os

os.system('cls')

try:
    connection = mysql.connector.connect(host='localhost',
                                        database='bd_certus',
                                        user='root',
                                        password='')
    print("Conexion exitosa!")

except mysql.connector.Error as e:
    print("Error en la consulta", e)
###########################################

def insert_into(_connection, _cod, _nom, _ape, _con):
    #print("INSERT INTO")

    _con = getpass.getpass("Contraseña: ")  # Solicitar la contraseña de forma segura
    sql_insert_Query = "insert into t_estudiantes(cod_estudiante, nom_estudiante, ape_estudiante, con_estudiante) values (%s, %s, %s, %s)"
    cursor = _connection.cursor()
    cursor.execute(sql_insert_Query, (_cod, _nom, _ape, _con))
    _connection.commit()
    print("Registro insertado!")


def select(_connection):
    #print("SELECT * FROM")
    sql_select_Query = "select * from t_estudiantes"
    cursor = _connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()

    for row in records:
        print("Codigo = ", row[0], )
        print("Nombre = ", row[1])
        print("Apellido  = ", row[2])
        print("Contraseña  = ", row[3], "\n")


def update(_connection, new_con, _cod_estudiante):
    #print("UPDATE")
    sql_update_Query = "update t_estudiantes set con_estudiante = %s where cod_estudiante = %s"
    cursor = _connection.cursor()
    cursor.execute(sql_update_Query, (new_con, _cod_estudiante))
    _connection.commit()
    print("Registro actualizado!")

def delete(_connection, _cod):
    #print("DELETE")
    sql_delete_Query = "delete from t_estudiantes where cod_estudiante = %s"
    cursor = _connection.cursor()
    cursor.execute(sql_delete_Query, (_cod,))
    _connection.commit()
    print("Registro eliminado!")


def menu_opciones():
    print("INICIO del CRUD")
    print("=====================")
    print("[1] Insertar")
    print("[2] Seleccionar")
    print("[3] Modificar")
    print("[4] Eliminar")
    print("[5] Salir del programa")
    print("=====================")

op = None
while op is None:
    try:
        op = int(input("Ingrese un opcion: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")

    if op == 1:
        print("Ingrese los datos del estudiante")
        _cod = input("Codigo: ")
        _nom = input("Nombres: ")
        _ape = input("Apellidos: ")
        _con = input("Contraseña: ")
        insert_into(connection, _cod, _nom, _ape, _con)

    elif op == 2:
        select(connection)
        
    elif op == 3:
        print("Modificar contraseña de estudiante")
        _cod = input("Codigo del estudiante: ")
        new_con = input("Nueva contraseña: ")
        update(connection, new_con, _cod)

    elif op == 4:
        print("Eliminar registro de estudiante")
        _cod_est = input("Codigo del estudiante: ")
        delete(connection, _cod_est)

    elif op == 5:
        print("FIN del CRUD")
        break; 

    print("===================================")
    rpt = input("Desea regresar al menu de opciones? s/n: ")

    if rpt == "s":
        #limpiar consola
        os.system('cls')
    else:
        exit()
    
else:
    print("FIN del CRUD")