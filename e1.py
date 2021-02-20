import string

def pangrama(oracion,abc):
  """Chequea si una funcion es un pangrama o no

  Args:
      oracion (String): Oracion que vamos a validar si es o no un pangrama
      abc (Set): Estructura de dato donde se encuentran las letras del abecedario en minuscula

  Returns:
      Bool: Retorna True si es un pangrama, False si no es un pangrama
  """
  for letra in abc:
    if letra not in oracion.lower():
      return False
  return True


def main():
  """Funcion de inicio del programa, inicializamos la variable alfabeto con las letras del abecedario ingles en minuscula y la variable oracion con lo que quisieramos validar si es o no un pangrama
  """
  alfabeto = set(string.ascii_lowercase)

  # Variables de prueba
  oracion = 'El cadaver de Wamba, rey godo de Espana, fue exhumado y trasladado en una caja de zinc que peso un kilo'
  # oracion = "Hola mundo"

  if pangrama(oracion,alfabeto):
    print("Es un pangrama!")
  else:
    print("No es pangrama!")


main()
