from datetime import datetime, timedelta

# ============================
# ESTUDIANTES
# ============================

ESTUDIANTES = [

    {
        "id": 1,
        "correo": "juan@epn.edu.ec",
        "password": "1234",
        "nombre": "Juan Pérez"
    },

    {
        "id": 2,
        "correo": "maria@epn.edu.ec",
        "password": "1234",
        "nombre": "María López"
    }

]


# ============================
# TAREAS
# ============================

TAREAS = [

    {
        "id": 1,
        "codigo": "PW001",
        "titulo": "Aplicación Flask",
        "descripcion": "Crear una aplicación Flask utilizando Docker.",
        "fecha_limite": datetime.now() + timedelta(days=2)
    },

    {
        "id": 2,
        "codigo": "BD001",
        "titulo": "Modelo Relacional",
        "descripcion": "Diseñar la base de datos del proyecto.",
        "fecha_limite": datetime.now() + timedelta(days=5)
    }

]


# ============================
# ENTREGAS
# ============================

ENTREGAS = []


# ============================
# MÉTODOS DE ACCESO A DATOS
# ============================

def obtener_estudiantes():
    return ESTUDIANTES


def obtener_tareas():
    return TAREAS


def obtener_tarea(id_tarea):

    for tarea in TAREAS:

        if tarea["id"] == id_tarea:
            return tarea

    return None


def obtener_entregas():
    return ENTREGAS


def guardar_entrega(entrega):
    ENTREGAS.append(entrega)