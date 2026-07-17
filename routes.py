from flask import render_template

import services


def configurar_rutas(app):

    @app.route("/")
    def login():

        return render_template("login.html")


    @app.route("/dashboard")
    def dashboard():

        tareas = services.listar_tareas()

        return render_template(
            "dashboard.html",
            tareas=tareas
        )


    @app.route("/tarea/<int:id_tarea>")
    def tarea(id_tarea):

        tarea = services.obtener_tarea(id_tarea)

        return render_template(
            "tarea.html",
            tarea=tarea,
            expirada=False,
            entregada=False
        )


    @app.route("/entrega/<int:id_tarea>")
    def entrega(id_tarea):

        entrega = {
            "titulo": "Aplicación Flask",
            "respuesta": "Respuesta de ejemplo",
            "fecha": "17/07/2026"
        }

        return render_template(
            "entrega.html",
            entrega=entrega
        )