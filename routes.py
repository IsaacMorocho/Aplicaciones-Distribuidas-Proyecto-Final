from flask import render_template
from App.database import tareas

def configurar_rutas(app):

    @app.route("/")
    def login():

        return render_template(
            "login.html"
        )


    @app.route("/dashboard")
    def dashboard():

        return render_template(
            "dashboard.html",
            tareas=tareas
        )


    @app.route("/tarea/<int:id>")
    def ver_tarea(id):

        tarea = next(
            (t for t in tareas if t["id"]==id),
            None
        )

        return render_template(
            "tarea.html",
            tarea=tarea,
            expirada=False,
            entregada=False
        )


    @app.route("/entrega/<int:id>")
    def ver_entrega(id):

        entrega={
            "titulo":"Aplicación Flask",
            "respuesta":"Respuesta simulada",
            "fecha":"17/07/2026"
        }

        return render_template(
            "entrega.html",
            entrega=entrega
        )