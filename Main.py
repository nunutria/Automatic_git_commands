import os
import subprocess
from io import open
from datetime import datetime
from plyer import notification

notification.notify(
    title='Automatic Contributions ',
    message='Starting Process...',
    app_icon= 'nunutria.ico',
    timeout= 5)

# Definimos nombres de archivos
ARCHIVO_TXT = "registroGitHub.txt"
ARCHIVO_BIN = "Contador.bin"

#Definir variables
RUTA_BASE = os.getcwd()
TIME = datetime.now()


# Funciones para manejo de archivos
def crear_archivo_txt(ruta, contenido):
    with open(ruta, "w") as archivo:
        archivo.write(contenido)

def crear_archivo_bin(ruta, valor_inicial):
    with open(ruta, "wb") as archivo:
        archivo.write(f"counter={valor_inicial}".encode())

def leer_valor_counter(ruta):
    with open(ruta, "rb") as archivo:
        contenido = archivo.read()
        indice = contenido.find(b"counter")
        return int(contenido[indice + 8:])

def actualizar_valor_counter(ruta, nuevo_valor):
    with open(ruta, "wb") as archivo:
        archivo.write(f"counter={nuevo_valor}".encode())

# Verificación y creación de archivos
if not os.path.isfile(os.path.join(RUTA_BASE, ARCHIVO_TXT)):
    crear_archivo_txt(os.path.join(RUTA_BASE, ARCHIVO_TXT), "Contenido inicial del archivo")

if not os.path.isfile(os.path.join(RUTA_BASE, ARCHIVO_BIN)):
    crear_archivo_bin(os.path.join(RUTA_BASE, ARCHIVO_BIN), 0)

# Agregar contenido al archivo TXT
with open(os.path.join(RUTA_BASE, ARCHIVO_TXT), "a") as archivo:
    archivo.write("\nCommit hecho en la fecha"+ str(TIME))

# Lectura y actualización del valor "counter"
valor_counter = leer_valor_counter(os.path.join(RUTA_BASE, ARCHIVO_BIN))
nuevo_valor = valor_counter + 1
actualizar_valor_counter(os.path.join(RUTA_BASE, ARCHIVO_BIN), nuevo_valor)

def realizar_commit(MENSAJE_COMMIT):
  subprocess.run(["git", "add", ARCHIVO_TXT])
  subprocess.run(["git", "commit", "-m", MENSAJE_COMMIT])
  subprocess.run(["git", "push", "origin", "main"])

MENSAJE_COMMIT = 'Update '+ ARCHIVO_TXT + ' en fecha ' + str(TIME)

realizar_commit(MENSAJE_COMMIT)

messageEnded = 'finalized process, contributions '+ str(nuevo_valor)+ ' in total'
notification.notify(
    title='Automatic Contributions ',
    app_icon= 'nunutria.ico',
    message=messageEnded)

