from datetime import datetime
from werkzeug.security import check_password_hash

import database


# ===============================
# LOGIN
# ===============================

def autenticar_usuario(correo, password):

    estudiantes = database.obtener_estudiantes()

    for estudiante in estudiantes:

        if estudiante["correo"] == correo and check_password_hash(estudiante["password"], password):
            return estudiante

    return None


# ===============================
# TAREAS
# ===============================

def listar_tareas():
    return database.obtener_tareas()


def obtener_tarea(id_tarea):
    return database.obtener_tarea(id_tarea)


# ===============================
# VALIDAR FECHA
# ===============================

def fecha_expirada(tarea):

    return datetime.now() > tarea["fecha_limite"]


# ===============================
# VALIDAR ENTREGA
# ===============================

def ya_entrego(id_estudiante, id_tarea):

    entregas = database.obtener_entregas()

    for entrega in entregas:

        if entrega["id_estudiante"] == id_estudiante and entrega["id_tarea"] == id_tarea:
            return True

    return False


# ===============================
# REGISTRAR ENTREGA
# ===============================

def registrar_entrega(id_estudiante, id_tarea, respuesta):

    entrega = {

        "id_estudiante": id_estudiante,
        "id_tarea": id_tarea,
        "respuesta": respuesta,
        "fecha_envio": datetime.now()

    }

    database.guardar_entrega(entrega)


# ===============================
# CONSULTAR ENTREGA
# ===============================

def obtener_entrega(id_estudiante, id_tarea):

    entregas = database.obtener_entregas()

    for entrega in entregas:

        if entrega["id_estudiante"] == id_estudiante and entrega["id_tarea"] == id_tarea:
            return entrega

    return None

def obtener_entregas_estudiante(id_estudiante):
    return database.obtener_entregas_estudiante(id_estudiante)