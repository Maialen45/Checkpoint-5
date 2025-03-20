#Ejercicio 1
nombres = ['Pedro', 'Ana', 'María']

for nombre in nombres:
    print(nombre)

#Ejercicio 2
def suma(num_one, num_two, num_three):
    return num_one + num_two + num_three

print(suma(1, 2, 3))

#Ejercicio 3
suma = lambda num_one, num_two, num_three: num_one + num_two + num_three
print(suma(1, 2, 3))

#Ejercicio 4:
nombre = 'Enrique'
lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

if nombre in lista_nombre:
    print('Coincide')
else:
    print('No coincide')