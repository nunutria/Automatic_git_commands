# Importamos las funciones open, read, exists y getcwd
import os
from io import open
from os.path import exists

# Obtenemos la ruta actual del directorio de trabajo
ruta_base = os.getcwd()

# Nombre del archivo
archivo_bin = "mi_archivo.bin"

# Combinamos la ruta base y el nombre del archivo
ruta_archivo_bin = os.path.join(ruta_base, archivo_bin)

# Verificamos si el archivo existe
if not exists(ruta_archivo_bin):
    print("El archivo", archivo_bin, "no existe. Creándolo...")

    # Creamos el archivo binario
    with open(ruta_archivo_bin, "wb") as archivo:
        # Escribimos la variable "counter" con el valor inicial
        archivo.write(b"counter=0")

    print("El archivo binario ha sido creado.")

# Leemos y actualizamos la variable "counter"
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
