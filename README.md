# Simulacro Parcial I

---

1. Dada una oración, escriba un programa Python para verificar si esa oración es un Pangrama o no. Un pangrama es una oración que contiene todas las letras del alfabeto inglés.
 4 Pts.

Luego, si la oración es un pangrama ordena de menor a mayor (A-Z) las letras usando uno de los algoritmos de ordenamiento (debe indicar cual está usando), y debe sólo mostrar caracteres no repetidos. 

Ejemplo de Input:
pangrama('El cadaver de Wamba, rey godo de Espana, fue exhumado y trasladado en una caja de zinc que peso un kilo')


Output:

['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

* Las letras del output deben ser de la oración del pangrama


Nota:
Puedes tener las letras del alfabeto con:

import string 

alfabeto = set(string.ascii_lowercase) 

---
---

2. Escriba una función que devuelva el número palíndromo* más cercano a un entero dado. Si dos números palíndromos empatan en distancia absoluta, devuelve el número más pequeño.
4 pts.

*Palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda, ejemplo: 101, 777, 22, 5

Ejemplo de input:
palindromo_cercano(27)
palindromo_cercano(100)

---
---

3. Te han contratado en Saman-Airlines ✈️, esta línea aérea desea llevar el control de las horas de sus pilotos para su respectivo pago; para esto, una vez que el piloto se presta a dar servicio, se toman los siguientes datos: cédula del piloto, tipo de avión (Hélice “H” o Jet “J”), y el número de horas del vuelo. Dependiendo de las horas se les paga a los pilotos. 

| Tipo de Avion    | Costo por hora |
| :---             | :----:         | 
| Helice           | 40             |
| Jet              | 50             | 


Usted deberá desarrollar un programa de forma de producir un output que contenga lo siguiente: 


**Para cada piloto:  4 Pts**
-Cédula de Identidad del piloto
-Tipo de avión 
-Monto Total a ser pagado al piloto. Si el piloto toma más de 8 horas de vuelo, se le otorgará un aumento del 10% sobre el Monto total a serle pagado. 

**Al final del día para la Samán Airlines: 7 Pts**
-La cantidad total de pilotos con su información 
-La cantidad de pilotos por tipo de avión 
-La cantidad de pilotos a quienes se les otorgó el aumento
-El Promedio de pago por tipo de avión 


---
