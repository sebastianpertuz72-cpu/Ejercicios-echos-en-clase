"""
print(" ".join(['Cristian', 'Daniel', 'Diaz', 'Bayona']))
 
"""
cad = input("Ingrese su numero de telefono con prefijo-numero-extension: ")
if "+" in cad[0] and "-" in cad[3] and "-" in cad[-3]:
    print(cad.split("-")[1])
else:
    print("Debe cumplir con el formato")
