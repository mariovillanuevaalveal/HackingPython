import requests

url = 'http://www.sitioweb.cl'  # Reemplaza con la URL del servidor que deseas verificar

try:
    response = requests.get(url)
    if response.status_code == 200:
        server_version = response.headers.get('Server')
        if server_version:
            print(f'La versión del servidor es: {server_version}')
        else:
            print('No se encontró información de versión del servidor en las cabeceras de respuesta.')
    else:
        print(f'La solicitud al servidor recibió un código de respuesta {response.status_code}.')
except requests.exceptions.RequestException as e:
    print(f'Error al hacer la solicitud al servidor: {e}')
