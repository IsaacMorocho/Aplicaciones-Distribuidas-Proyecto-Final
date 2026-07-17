from flask import Flask
from routes import configurar_rutas

app = Flask(__name__)
app.secret_key = "admin123"

configurar_rutas(app)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )