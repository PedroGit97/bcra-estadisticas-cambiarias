# ¿ Por que el nombre bcra-estadisticas-cambiarias ?

- bcra --> institución fuente (Banco Central de la República Argentina)
- estadisticas --> naturaleza del contenido (datos oficiales)
- cambiarias --> dominio especifico (mercados de cambios/FX)

# Estructura de la Carpeta 📂

bcra-estadisticas-cambiarias/
 |_ README.md
 |_ requirements.txt  # librerias necesarias para este proyecto
 |_ .gitignore
 |_ src/
    |_ bcra_ec/
    |   |_ _init_.py
    |   |_ client.py
    |_ main.py

# ¿ Que aprendí con este proyecto ?

## requirement.txt
    Es un archivo de texto plano que lista las dependencias externas que mi proyecto necesita para funcionar.

    Permite que lo pueda reproducir en el futuro y que controle las versiones.

    Si algún librería cambia en el futuro, este código podría no funcionar por eso se necesita la versión exacta de la libreria.

    Este código depende de librerías que no viene con Python estandar


# Pasos de este proyecto 🛣️

1. Crear un **Entorno Virtual** + **dependencias**

    - Así aislo el proyecto
    - Evito conflicto de versiones
    - Hace reproducible mi trabajo

1.2 Crear y activar 'Entorno Virtual'
 - Windows:
    - python -m venv .venv [X]
    - .venv\Scripts\activate [X]
 - macOS\Linux:
   - python3 -m venv .venv
   - source .venv/bin/activate

1.2.1 ¿ Como saber si estoy dentro del **Entorno Virtual** ?

Cuando activás el entorno virtual, tu terminal cambia.
Ejemplo: 
(.venv) C:\Users\Pedro\bcra-estadisticas-cambiarias>

Para comprobar usar:

where python

Si estás dentro del entorno virtual, la ruta debería apuntar a algo como:

.../bcra-estadisticas-cambiarias/.venv/Scripts/python.exe