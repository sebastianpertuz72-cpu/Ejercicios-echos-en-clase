ruta = "/home/camper/Documentos/diccionarios/lectura-archivos/"
with open(ruta + "texto2.txt", "w") as arch:
    arch.write("Hola")
    arch.write("mundo\n")
    arch.write("Grupo C4 :D")
    
    # writelines()
    arch.write("\n")
    tpl = ("Jorge\n", "Eduardo\n", "Kari\n", "Linderman\n")
    arch.writelines(tpl) # o tmb en vez de tanto\n se puede hacer: arch.writelines("\n".join(tpl))
    