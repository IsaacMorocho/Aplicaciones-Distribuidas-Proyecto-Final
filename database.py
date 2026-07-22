import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', 'root'),
        database=os.getenv('DB_NAME', 'app_db')
    )

# ============================
# MÉTODOS DE ACCESO A DATOS
# ============================

def obtener_estudiantes():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    # Renombramos campos para mantener compatibilidad con services.py
    cursor.execute("SELECT id, username as correo, password_hash as password FROM students")
    estudiantes = cursor.fetchall()
    conn.close()
    return estudiantes


def obtener_tareas():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, codigo, titulo, descripcion, fecha_limite FROM tasks")
    tareas = cursor.fetchall()
    conn.close()
    return tareas


def obtener_tarea(id_tarea):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, codigo, titulo, descripcion, fecha_limite FROM tasks WHERE id = %s", (id_tarea,))
    tarea = cursor.fetchone()
    conn.close()
    return tarea


def obtener_entregas():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    # Renombramos para compatibilidad con services.py
    cursor.execute("SELECT id, student_id as id_estudiante, task_id as id_tarea, respuesta, fecha_entrega as fecha_envio FROM submissions")
    entregas = cursor.fetchall()
    conn.close()
    return entregas


def guardar_entrega(entrega):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO submissions (student_id, task_id, respuesta, fecha_entrega)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (entrega['id_estudiante'], entrega['id_tarea'], entrega['respuesta'], entrega['fecha_envio']))
    conn.commit()
    conn.close()