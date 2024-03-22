import os

# Nombre del archivo
archivo_txt = "mi_archivo.txt"

# Ruta del archivo (opcional)
ruta_archivo = os.path.join("C:", "Users", "SamUrbina", "Desktop", "Python", archivo_txt)

# Verifica si el archivo existe
if os.path.exists(ruta_archivo):
    print("El archivo", archivo_txt, "ya existe.")
else:
    print("El archivo", archivo_txt, "no existe. Creándolo...")

    # Crea el archivo
    with open(ruta_archivo, "w") as archivo:
        archivo.write("Contenido inicial del archivo")


    print("El archivo", archivo_txt, "ha sido creado.")

# Agrega contenido al archivo
with open(ruta_archivo, "a") as archivo:
    archivo.write("\nNueva línea de contenido")

print("Se ha añadido contenido al archivo", archivo_txt)
