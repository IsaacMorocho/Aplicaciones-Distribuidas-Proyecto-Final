from flask import render_template, request, session, redirect, url_for

import services


def configurar_rutas(app):

    @app.route("/")
    def login():

        return render_template("login.html")


    @app.route("/login", methods=["POST"])
    def do_login():
        correo = request.form.get("correo")
        password = request.form.get("password")
        
        usuario = services.autenticar_usuario(correo, password)
        if usuario:
            session['usuario_id'] = usuario['id']
            session['username'] = usuario['correo']
            return redirect(url_for('dashboard'))
        
        return render_template("login.html", error="Credenciales incorrectas")


    @app.route("/dashboard")
    def dashboard():
        if 'usuario_id' not in session:
            return redirect(url_for('login'))

        tareas = services.listar_tareas()
        
        for tarea in tareas:
            tarea['expirada'] = services.fecha_expirada(tarea)

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