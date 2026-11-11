"""
Un programa que lance 10.000.000 veces dos datos y
muestre cual es el numero que mas cae
"""
import random

lanzamientos = 10_000_000

#crear un diccionario que almacene 
frecuencia = {}
for dado in range(2, 13):
    frecuencia[dado] = 0
    
for i in range(lanzamientos):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1,6)
    suma = dado1 + dado2
    
    frecuencia[suma] += 1

mas_cae = 0
veces = 0
for dado, valor in frecuencia.items():
    if valor > veces:
        mas_cae = dado
        veces = valor
        
print("El dado que mas cae es: ", mas_cae)
print("La cantidad de veces que cayo es: ", veces)