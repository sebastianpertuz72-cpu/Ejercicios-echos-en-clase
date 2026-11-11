import json

ruta = "/home/camper/Documentos/"
nom_arch = ruta + "datos.json"

with open(nom_arch, "r", encoding="utf-8") as arch:
    lista = json.load(arch)
    
print("Cargue de la lista terminada")
print(lista)
print(type(lista))

print("Cargando estudiantes...")

nom_arch = ruta + "estudiantes.json"
with open(nom_arch, "r", encoding="utf-8") as arch:
    dicc_est = json.load(arch)
    
print(dicc_est)
print(type(dicc_est))
print("Cantidad de estudiantes: ", len(dicc_est))
print("Nombres de los estudiantes; ",
    dicc_est[0]["nombre"],
    dicc_est[1]["nombre"],
    dicc_est[2]["nombre"])