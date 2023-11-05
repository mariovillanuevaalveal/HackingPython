import requests
import time

# Especifica el dominio base que deseas verificar
dominio_base = "dominio.cl"

# Abre el archivo de wordlist
with open('Subdomain.txt', 'r') as archivo:
    with open('dominios_exitosos.txt', 'w') as exitosos:
        for linea in archivo:
            subdominio = linea.strip()  # Elimina espacios en blanco y saltos de línea
            url = f"http://{subdominio}.{dominio_base}"  # Construye la URL completa

            try:
                response = requests.get(url)
                if response.status_code == 200:
                    print(f"{url} responde con código 200 OK")
                    # Registra los dominios exitosos dentro del archivo 'dominios_exitosos.txt'
                    exitosos.write(f"{url}\n")
                else:
                    print(f"{url} responde con código {response.status_code}")
            except requests.exceptions.RequestException:
                pass

            # Espera 0.5 segundos antes de la siguiente consulta
            # para evitar ser detectado como tráfico malicioso 
            time.sleep(0.5)

# Cierra automáticamente los archivos
