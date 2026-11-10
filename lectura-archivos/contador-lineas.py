ruta_arch = "/home/camper/Documentos/diccionarios/lectura-archivos/mbox.txt"

with open(ruta_arch, "r") as arch:
    cont = 0
    for linea in arch:
        cont += 1
    print(f"Cantidad lineas {cont:,}") #formato de que aestacosa: separar por ,