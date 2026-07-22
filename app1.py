import os
from flask import Flask
from routes import configurar_rutas
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "admin123")

import socket
@app.context_processor
def inject_hostname():
    return dict(nodo_atendido=socket.gethostname())

configurar_rutas(app)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )