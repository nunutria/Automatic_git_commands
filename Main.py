#test
import os
from io import open
from os.path import exists

# Definimos nombres de archivos
archivo_txt = "registroCommit.txt"
archivo_bin = "counter.bin"

#Obtenemos la ruta actual del archivo
ruta_base = os.getcwd()

#establecemos la ruta junto con el nombre del archivo
ruta_archivo_bin = os.path.join(ruta_base, archivo_bin)
ruta_archivo_txt = os.path.join(ruta_base, archivo_txt)

#condiciona para la existencia del archivo TXT'
if os.path.exists(ruta_archivo_txt):
    print("El archivo", archivo_txt, "ya existe.")
else:
    print("El archivo", archivo_txt, "no existe. Creándolo...")

    # Crea el archivo
    with open(ruta_archivo_txt, "w") as archivo:
        archivo.write("Contenido inicial del archivo")

    print("El archivo", archivo_txt, "ha sido creado.")

#condiciona para la existencia del archivo BIN 
if not exists(ruta_archivo_bin):
    print("El archivo", archivo_bin, "no existe. Creándolo...")

    # Creamos el archivo binario
    with open(ruta_archivo_bin, "wb") as archivo:
        # Escribimos la variable "counter" con el valor inicial
        archivo.write(b"counter=0")

    print("El archivo binario ha sido creado.")
# Agrega contenido al archivo TXT
with open(ruta_archivo_txt, "a") as archivo:
    archivo.write("\nNueva línea de contenido")

print("Se ha añadido contenido al archivo", archivo_txt)


#bloque de código operación para archivo BIN
# Leemos y actualizamos la variable "counter" del archivo BIN
try:
    # Abrimos el archivo en modo lectura binaria
    with open(ruta_archivo_bin, "rb") as archivo:
        # Leemos el contenido del archivo
        contenido = archivo.read()

    # Buscamos la variable "counter" en el contenido del archivo
    indice_counter = contenido.find(b"counter")
    valor_counter = int(contenido[indice_counter + 8:])

except ValueError:
    # Si no se encuentra la variable "counter" en el archivo
    print("La variable 'counter' no se encuentra en el archivo. Inicializando...")
    valor_counter = 1

# Actualizamos el valor de la variable "counter"
nuevo_valor = valor_counter + 1

# Abrimos el archivo en modo escritura binaria
with open(ruta_archivo_bin, "wb") as archivo:
    # Escribimos la variable "counter" con el nuevo valor
    archivo.write("counter={}".format(nuevo_valor).encode())

# Mostramos las veces que se ha ejecutado el script
print("El script se ha ejecutado", nuevo_valor, "veces.")

print("El valor de la variable 'counter' ha sido actualizado a:", nuevo_valor)

print("El script se ha ejecutado correctamente.")


