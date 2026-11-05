listanum=[]

def busqueda_linear(line, mambo):
    for i, matikane in enumerate(line, 0):
        if matikane == mambo:
            return i
    return None

for i in range(10000):
    listanum.append(i+1)

    
mambo = int(input("INgrese un numero"))
encontrar = busqueda_linear(listanum, mambo)
print(encontrar)