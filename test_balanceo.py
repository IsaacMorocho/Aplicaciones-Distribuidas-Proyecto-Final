import requests
import re
from collections import Counter

counts = Counter()
url = "http://localhost/"
total_requests = 60

print(f"Enviando {total_requests} peticiones a {url}...")
for _ in range(total_requests):
    try:
        response = requests.get(url)
        # Regex mejorado para soportar guiones en el hostname por si acaso
        match = re.search(r"Atendido por:\s*([a-zA-Z0-9_-]+)", response.text)
        if match:
            counts[match.group(1)] += 1
    except Exception as e:
        print("Error de conexión:", e)

print("\n--- Resultados ---")
if not counts:
    print("ADVERTENCIA: El regex no encontro coincidencias en ninguna de las respuestas.")
    print("Por favor revisa si la aplicacion esta caida o si el HTML del footer cambio.")
else:
    print("Resultados de distribución (Esperado aprox: app1=50%, app2=33%, app3=17%):")
    for node, count in counts.most_common():
        porcentaje = (count / total_requests) * 100
        print(f"- {node}: {count} peticiones ({porcentaje:.1f}%)")
