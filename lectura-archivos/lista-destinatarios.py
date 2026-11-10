"""
Cree un archivo de texto con los destinatarios sin repetir, ordenados alfabeticamente

"""

ruta_arch = "/home/camper/Documentos/diccionarios/lectura-archivos/mbox.txt"

ruta_dest = "/home/camper/Documentos/diccionarios/lectura-archivos/destinatarios.txt"



with open(ruta_arch, "r", encoding="utf-8") as arch, \
    open(ruta_dest, "w", encoding="utf-8") as dest:
    emails = set()
    for linea in arch:
        if linea.startswith("To:"):
            emails.add(linea.split(" ")[1])
            
    
    lst_email = list(emails)
    lst_email.sort
    
    dest.writelines(lst_email)
            
