def es_palindromo(n):
  """Calcula si un numero n dado es palindromo o no

  Args:
      n (int): Numero entero dado

  Returns:
      Bool: Retorna True si es palindromo, False si no es palindromo
  """

  if str(n)[::-1] == str(n):
    return True
  return False

def palindromo_cercano(n):
  """Dado un numero n buscamos cual es su palindromo mas cercano

  Args:
      n (int): Numero entero
  """

  # Aca empiezan los calculos para ver cual es el palindromo mas cercano hacia abajo del numero
  target_abajo = n
  contador_abajo = 0

  while True:

      if es_palindromo(target_abajo):
          break
      target_abajo -= 1
      contador_abajo += 1

  # Chequeamos cual es el palindromo mas cercano hacia arriba del numero
  target_arriba = n
  contador_arriba = 0

  while True:
      if es_palindromo(target_arriba):
          break
      target_arriba -= 1
      contador_arriba += 1

  # Luego de haber calculado el palindromo cercano arriba y abajo chequeamos cual es el mas cercano
  if contador_abajo <= contador_arriba:
      print(f"El palindromo mas cercano a {n} es {target_abajo}")
  else:
      print(f"El palindromo mas cercano a {n} es {target_arriba}")

def main():
  """Funcion de inicio del programa, inicializamos la variable n con un numero para chequear cual es su palindromo mas cercano
  """
  n = 100
  palindromo_cercano(n)


main()
