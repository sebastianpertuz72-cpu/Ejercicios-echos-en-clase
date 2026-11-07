#como crear un diccionario

midicc = {} #diccionario vacio
otraformadedict = dict() #otro diccionario vacio

#definiendo
capitales = {"Colombia":"Bogotta", "Peru":"Lima", "Venezuela":"Caracas"}

#Crear una nueva entrada
capitales["Argentina"] = "Buenos Aires"

print(capitales)

# editar un valor
capitales["Colombia"] = "Santa fe de Bogota"
print(capitales)

# Borrar una llave: valor
del capitales["Venezuela"]
print(capitales)

# get(): accede a un valor y opcionalmente puede devolver un valor si no esta.

try:
    capitales["España"]
except:
    print("Error. la llave no se encuentra en el diccionario.")
    
print(capitales.get("España","No existe la llave en el diccionario."))

#Keys( : lista todas las claves del diccionario
print(list(capitales.keys()))

#values(): lista todos los valores del diccionario
print(capitales.values())

#items(): devuelve todos los pares (clave, valor)
print(capitales.items())

for pais, capital in capitales.items():
    print(f"la capital de {pais} es {capital}")
    
# update(): Incorpora varias clave,valor desde otro diccionario
capitales_europa = {"Portugal":"Lisboa", "España":"Madrid", "Francia":"Paris"}
capitales.update(capitales_europa)
print(capitales)

# setdefault(): Si existe la llave, devuelve el valor, sino existe, la crea con un valor.

print(capitales.setdefault("España","Barcelona"))
print(capitales.setdefault("Alemania", "Berlin"))
print(capitales)

# pop(): elimina pero devuelve el valor eliminado
print(capitales.pop("Alemania"))
print(capitales)

# popitem(): Elimina y deuelve el ultimo par insertado
print(capitales.popitem())
print(capitales)

# len(): cuenta cuantas pares clave-valor hay en el diccionario
print(len(capitales))

#fromkeys(): Genera un diccionario donde todas las claves comparten el mismo valor inicial
pobl_paises = dict.fromkeys(capitales, 0)
print(pobl_paises)