# Leer 10 enteros, almacenarlos en un vector y determinar en qué posición del vector está el mayor número primo leído.
numeros = []
numeros_primos = []
es_primo = True


for z in range(1, 11):
    numero = int(input(f'Entero {z}: '))
    numeros.append(numero)
    
for i in numeros:
    for y in range(2, i):
        if i % y == 0:
            es_primo = False
            break
    
    if es_primo and i > 1:
        numeros_primos.append(i)
  
max_primo = max(numeros_primos)
indice = numeros_primos.index(max_primo)
print(f'El número primo mayor {max_primo}, se encuentra en la posición {indice}.')