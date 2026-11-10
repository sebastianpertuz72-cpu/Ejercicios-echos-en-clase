# 1. Apertura
arch = open("/home/camper/Documentos/diccionarios/lectura-archivos/texto.txt", "r")

# 2. Manipulacion
info = arch.read()
print(info)

arch.seek(0) # ubica el cursor del archivo al inicio de este
info = arch.read(1)
print(info)

#READLINE()

info = arch.readline()
print(info)

print("----FOR----")
for linea in arch:
    print(linea.strip())
    
print("----WHILE----")
arch.seek(0)
info = arch.readline()
while info:
    print(info.strip())
    info = arch.readline()
    
#readlines()
arch.seek(0)
lineas = arch.readlines()
print(lineas)
    
#3. El cierre
arch.close()