ruta_arch = "/home/camper/Documentos/diccionarios/lectura-archivos/mbox.txt"

with open(ruta_arch, "r") as arch:
    cont = 0
    emails = set()
    for linea in arch:
        if linea.startswith("From:"):
            cont += 1
            emails.add(linea.split(" ")[1])
    print(f"Cantidad correo: {cont:,}")
    print(f"Cantidad correos con origen distintos: {len(emails):,}")