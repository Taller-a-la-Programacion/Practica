# Practicas

## Instrucciones Generales
- El archivo **debe** llamarse **Practicas.py**
- **Debe** respetar el nombre de las funciones y el nombre de los parámetros que más adelante se describen
- Deben contruir las funciones con **Python**
- Debe crear los comentarios de cada función tomando en cuenta **Nombre**, **Entrada**, **Salida** y **Restricciones**


## Convertir Número

Escribir un programa con sintaxis Python cuya función principal se llame **convertirNumero(num, exponente)**, reciben dos números **enteros cualquiera** y retorne un nuevo número con la siguiente lógica:
- Sea el número num = 12558 y exponente = 4
- El total de dígitos de **num** debe ser **IMPAR**
- Se obtiene el dígito del medio (5) y aplica la potencia según su **exponente** es decir, 5 ** 4 = 625
- El extremo izquierdo (12) formará un nuevo número solo con los dígitos **impares**, es decir 1
- El extremo derecho (58) formará un nuevo número solo con los dígitos **pares**, es decir 8
- El nuevo número a formar sería el siguiente: 16258
- En el caso de no existir pares o impares, se concatena con CERO

```python
>>> convertirNumero(12558, 4)
16258
>>> convertirNumero(-94161, 5) #-9 1 6
-916
>>> convertirNumero(8517210, 5) #51 16807 20
511680720
>>>convertirNumero('8517210', 5)
511680720
```


##	Invertir elementos lista
Escriba un programa con sintaxis Python cuya función principal se llame **invertirLista(lista)**, que reciba como entrada una lista con números enteros denominado **lista** y que retorne la lista pero con los elementos invertidos 


```python
>>>invertirLista([5,8,45,96])
[96, 45, 8, 5]

>>> invertirLista([56, 85,8,45,96])
[96, 45, 8, 85, 56]

>>> invertirLista([])
"Error: La lista debe contener al menos 2 elementos"

>>> invertirLista([2,5,7,"ABC"])
"Error: La lista debe elementos tipo entero"
```

##	Elemento menor y mayor de la lista
Escriba un programa con sintaxis Python cuya función principal se llame **extremosLista(lista)**, que reciba como entrada una lista con números enteros denominado **lista** y que retorne la lista con 2 elementos donde ellos serán el número menor y mayor de la lista

```python
>>>extremosLista([18,5,8,45,96, 60])
[5,96]

>>> extremosLista([96, 96,96])
[96]

>>> extremosLista([])
"Error: La lista debe contener al menos 2 elementos"
