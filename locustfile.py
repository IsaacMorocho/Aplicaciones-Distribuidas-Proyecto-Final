import re
from locust import HttpUser, task, between

class EstudianteUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        self.client.post("/login", data={
            "correo": "juan@epn.edu.ec",
            "password": "1234"
        })

    @task
    def ver_dashboard(self):
        response = self.client.get("/dashboard")
        match = re.search(r"Atendido por:\s*(\w+)", response.text)
        if match:
            print(f"Nodo atendido: {match.group(1)}")
