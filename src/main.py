import requests

url = "https://api.bcra.gob.ar/estadisticascambiarias/v1.0/Maestros/Divisas"

response = requests.get(url)

print(response.json())
