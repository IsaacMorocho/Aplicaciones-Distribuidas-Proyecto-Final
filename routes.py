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


    @app.route("/tarea/<int:id_tarea>", methods=["GET", "POST"])
    def tarea(id_tarea):
        if 'usuario_id' not in session:
            return redirect(url_for('login'))

        tarea = services.obtener_tarea(id_tarea)
        if not tarea:
            return redirect(url_for('dashboard'))
            
        usuario_id = session['usuario_id']
        entrega = services.obtener_entrega(usuario_id, id_tarea)
        entregada = entrega is not None
        expirada = services.fecha_expirada(tarea)

        if request.method == "POST":
            if expirada:
                return render_template("tarea.html", tarea=tarea, expirada=expirada, entregada=entregada, entrega=entrega, error="El plazo de entrega ha expirado")
            
            if entregada:
                return render_template("tarea.html", tarea=tarea, expirada=expirada, entregada=entregada, entrega=entrega, error="Ya registraste una entrega para esta tarea")
            
            respuesta = request.form.get("respuesta")
            services.registrar_entrega(usuario_id, id_tarea, respuesta)
            
            # Refetch entrega after successful submission
            entrega = services.obtener_entrega(usuario_id, id_tarea)
            return render_template("tarea.html", tarea=tarea, expirada=expirada, entregada=True, entrega=entrega, success="Entrega registrada exitosamente")

        return render_template(
            "tarea.html",
            tarea=tarea,
            expirada=expirada,
            entregada=entregada,
            entrega=entrega
        )


    @app.route("/entregas")
    def entregas():
        if 'usuario_id' not in session:
            return redirect(url_for('login'))

        usuario_id = session['usuario_id']
        mis_entregas = services.obtener_entregas_estudiante(usuario_id)

        return render_template(
            "entregas.html",
            entregas=mis_entregas
        )