import json

ruta = "/home/camper/Documentos/"
nom_arch = ruta + "datos.json"

lista = [10,4,15,50,30]

with open(nom_arch, "w", encoding="utf-8") as archivo:
    json.dump(lista, archivo)
    
nom_arch2 = ruta + "estudiantes.json"

estudiantes = [
    {"nombre":"Ana", "edad":19, "curso":"Python"},
    {"nombre":"Luis", "edad":21, "curso":"Introduccion a la programacion"},
    {"nombre":"pana", "edad":29, "curso":"Python"},
]

with open(nom_arch2,"w", encoding="utf-8") as archivo:
    json.dump(estudiantes, archivo, indent=4)
    
print("Proceso terminado.")