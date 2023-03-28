# 2021 Semestre 2
# Portafolio 2 Parte A

## Instrucciones Generales
- El archivo **debe** llamarse **Portafolio2A.py**
- **Debe** respetar el nombre de las funciones y el nombre de los parámetros que más adelante se describen
- Deben contruir las funciones con **Python**
- Debe utilizar la programación **Recursiva de COLA**
- Debe crear los comentarios de cada función tomando en cuenta **Nombre**, **Entrada**, **Salida** y **Restricciones**
- Fecha de entrega: **Viernes 24 de Setiembre a las 10pm**

##	Número abundante
Escriba un programa con sintaxis Python cuya función principal se llame **numeroAbundante(num)**, que reciba como entrada un número entero positivo denominado **num** y que retorne si cumple (True) o no los requisitos (False) de número abundante. 
Un número abundante es un número natural y que la suma de sus divisores es mayor que su duplo, es decir:
-	El valor de **num** será 12 y sus divisores son (1,2,3,4,6 y 12)
-	La suma de ellos son 1+2+3+4+6+12 = 28
-	Entonces el 12 es un número abundante porque la suma de sus divisores 28 y es mayor que el duplo de 12, es decir 24. (28 > 12 x 2)

```python
>>>numeroAbundante(12)
True
>>> numeroAbundante (8)
False
>>> numeroAbundante (-8)
"Error: La entrada, debe ser número positivo"
```

##	Suma Adyacentes Impar 

Escriba un programa con sintaxis Python cuya función principal se llame **adyacentesImpares(num)**, recibe un número **entero positivo** y debe retornar **True** en caso de que todas las sumas de **dos dígitos adyacentes sean impares**, retornar **False** en caso de que alguna suma de adyacentes **no sea impar**, es decir:
- Sea num = 9252783
  - Agrupar cada 2 dígitos y sumarlos cada uno de ellos: 3+8, 7+2, 5+2, 9 y el resultado de cada una de esas suma son: 11, 9, 7, 9
  - Como se puede apreciar todos esos resultados son impares, por lo tanto la respuesta es **True**

```python
>>> adyacentesImpares (9252783) 
True 
>>> adyacentesImpares (51730)
False
>>> adyacentesImpares (5836)
True
>>> adyacentesImpares (-9)
"Error: Número debe ser positivo"
```

## Convertir Número

Escribir un programa con sintaxis Python cuya función principal se llame **convertirNumero(num, exponente)**, reciben dos números **enteros cualquiera** y retorne un nuevo número con la siguiente lógica:
- Sea el número num = 12558 y factor = 4
- El total de dígitos de **num** debe ser **IMPAR**
- Se obtiene el dígito del medio (5) y aplica la potencia según su **exponente** es decir, 5 ** 4 = 625
- El extremo izquierdo (12) formará un nuevo número solo con los dígitos **impares**, es decir 1
- El extremo derecho (58) formará un nuevo número solo con los dígitos **pares**, es decir 8
- El nuevo número a formar sería el siguiente: 16258
- En el caso de no existir pares o impares, el resultado será de CERO

```python
>>> convertirNumero(12558, 4)
16258
>>> convertirNumero(-94161, 5) #-9 1 6
-916
>>> convertirNumero(8517210, 5) #51 16807 20
511680720
>>>convertirNumero('8517210', 5)
"Error: Debe ser entero"
```
  
##	Comprimir Número 
Escriba un programa con sintaxis Python cuya función principal se llame **comprimirNumero(num)**, recibe un número **entero** y debe retornar un nuevo número quitando aquellos dígitos **repetidos** en este, es decir:
- Sea num = 15532, el **dígito 5** se aparece más de una vez por lo tanto será eliminado, dando como resultado, **1532**
- Sea num = 82581534, los **dígitos 8 y 5** se aparecen más de una vez por lo tanto serán eliminados, dando como resultado, **825134**

```python
>>> comprimirNumero (15532) 
1532 
>>> comprimirNumero (82581534) 
281534
>>> comprimirNumero (-82581534) 
-281534
>>>comprimirNumero('82581534')
"Error: Debe ser entero"
```

##	Número Hermano 

Escriba un programa con sintaxis Python cuya función principal se llame **numeroHermano(num)**, que reciba como entrada un número entero positivo denominado **num** y que retorne si cumple (True) o no los requisitos (False) de número hermano. 
Un número hermano es un número natural y que posee dos divisores primos. No tomar en cuenta el 1 por que no es primo y el mismo **num**:
-	El valor de **num** será 20 y sus divisores son (1,2,4,5,10 y 20) pero no se toman en cuenta 1 y 20
-	De los números divisores 2,4,5 y 10 el 2 y 5 son números primos, por lo tanto es **True**
-	El valor de **num** será 8 y sus divisores son (1,2,4, y 8) pero no se toman en cuenta 1 y 8
-	De los números divisores 2 y 4 solo el 2 es número primos, por lo tanto no cumple con el requisito de al menos 2 divisores que sean primos, por lo tanto es **False**

```python
>>>numeroHermano(20) 
True
>>> numeroHermano (8) 
False
>>> numeroHermano (-8)
"Error: El número debe ser positivo"
```

##	Suma Adyacentes Pares

Escriba un programa con sintaxis Python cuya función principal se llame **adyacentesPares(num)**, recibe un número **entero positivo** y debe retornar **True** en caso de que todas las sumas de **dos dígitos adyacentes sean pares**, retornar **False** en caso de que alguna suma de adyacentes **no sea par**, es decir:
- Sea num = 6241753
  - Agrupar cada 2 dígitos y sumarlos cada uno de ellos: 5+3,1+7,2+4, 6 y el resultado de cada una de esas suma son: 8, 8, 6 y 6
  - Como se puede apreciar todos esos resultados son pares, por lo tanto la respuesta es **True**

```python
>>> adyacentesPares (6241753) 
True 
>>> adyacentesPares (32820)
False
>>> adyacentesPares (5726)
True
>>> adyacentesPares (-9)
"Número no se puede procesar"
```

## Convertir Número 2 

Escribir un programa con sintaxis Python cuya función principal se llame **convertirNumero(num, factor)**, reciben dos números **enteros cualquiera** y retorne un nuevo número con la siguiente lógica:
- Sea el número num = 25682525 y factor = 4
- El total de dígitos de **num** debe ser **PAR**
- Se obtiene los dos dígitos del medio (82) y se multiplica por el **factor** es decir, 82 * 4 = 328
- El extremo derecho (525) formará un nuevo número solo con los dígitos **impares**, es decir 55
- El extremo izquierdo (256) formará un nuevo número solo con los dígitos **pares**, es decir 26
- El nuevo número a formar sería el siguiente: 2632855
- En el caso de no existir pares o impares, el resultado será de CERO

```python
>>> convertirNumero2(25682525, 4)
2632855
>>> convertirNumero2(-943161, 3)
-4931
>>> convertirNumero2(7210, 10)
2100
>>> convertirNumero2('7210', 10)
"Error: Debe ser entero"
```

##	Super Primo 
Escriba un programa con sintaxis Python cuya función principal se llame **superPrimo(num)**, que reciba como entrada un número **entero positivo** denominado **num** y que retorne si cumple (True) o no los requisitos (False) de número súper primo. 
Un número súper primo es un número natural que la suma de sus dígitos impares sea **primo**.

-	El valor de **num** será 37823 y sus la suma de sus digitos son (3 + 7 + 3) 
-	La suma de ellos es 13 y por lo tanto es primo, entonces es **True**


```python
>>>superPrimo(12)
False
>>> superPrimo (807491)
True
>>> superPrimo (-8)
"Error: El número debe ser positivo"
```

##	Suma Adyacentes 

Escriba un programa con sintaxis Python cuya función principal se llame **adyacentes(num)**, recibe un número **entero positivo** y debe retornar **True** en caso de que todas las sumas de **dos dígitos adyacentes sean DIVISIBLE entre 3**, retornar **False** en caso de que alguna suma de adyacentes **no sea par**, es decir:
- Sea num = 6242754
  - Agrupar cada 2 dígitos y sumarlos cada uno de ellos: 5+4, 2+7, 2+4, 6 y el resultado de cada una de esas suma son: 9, 9, 6 y 6
  - Como se puede apreciar todos esos resultados son divisibles entre TRES, por lo tanto la respuesta es **True**

```python
>>> adyacentes (6242754) 
True 
>>> adyacentes (41830)
False
>>> adyacentes (8736)
True
>>> adyacentes (-9)
"Error: Número debe ser positivo"
```

## Convertir Número 3 

Escribir un programa con sintaxis Python cuya función principal se llame **convertirNumero(num, factor)**, reciben dos números **enteros cualquiera** y retorne un nuevo número con la siguiente lógica:
- Sea el número num = 25682525 y factor = 4
- El total de dígitos de **num** debe ser **PAR**
- Se obtiene los dos dígitos del medio (82) y se aplica la división entera, es decir, 82 // 4 = 20
- El extremo derecho (525) formará un nuevo número solo con los dígitos **impares**, es decir 55
- El extremo izquierdo (256) formará un nuevo número solo con los dígitos **pares**, es decir 26
- El nuevo número a formar sería el siguiente: 2632855
- En el caso de no existir pares o impares, el resultado será de CERO

```python
>>> convertirNumero3(25682525, 4)
262055
>>> convertirNumero3(-943161, 3) # -4, 31//3, 1 
-4101
>>> convertirNumero3(7210, 10) # 0, 21//10, 0
20
>>> convertirNumero3('7210', 10)
"Error: Debe ser entero"
```
