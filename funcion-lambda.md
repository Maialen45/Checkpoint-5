# Función lambda

La función lambda permite empaquetar una función pequeña y meterla en una función más grande. Se utilizan cuando tenemos una función pequeña que vamos a utilizar repetidas veces. Por ejemplo si tenemos la siguiente función: 
```sh
def nombre_completo(nombre, apellido):
    print(f'Hola {nombre} {apellido}')

nombre_completo('Pedro', 'García')
```
![Lambda normal](Images/lambda-normal.png)

En este caso tenemos una función con la cual saludamos a una persona. Esta función tiene dos argumentos, el nombre y el apellido. Podríamos crear una variable que contenga la función lambda de forma que metamos el nombre completo en otra función. Posteriormente, podremos anidar el nombre completo en la función ```saludo```.
```sh
nombre_completo = lambda nombre, apellido: f'{nombre} {apellido}'

def saludo(nombre_completo):
    print(f'Hola {nombre_completo}')

saludo(nombre_completo('Pedro', 'García'))
```
![Lambda function](Images/lambda-function.png)

La forma de escribir la función lambda es la siguiente. Creamos una variable en la cual escribimos ```lambda``` seguido de los argumentos que tendrá la función. Después de los dos puntos escribimos el resultado que queremos obtener de la función. Para anidar esta función dentro de la de ```saludo``` solo tendremos que llamarla entre llaves {}. A la hora de obtener el resultado, también hay que tener en cuenta que hay que anidar una función dentro de otra, es decir, primero llamamos la función ```saludo``` y dentro de esta llamamos la función ```nombre_completo``` con sus dos argumentos ```(saludo(nombre_completo('Pedro', 'García')))```.
