def es_pronico(n):
  """Calcula si un numero n dado es pronico o no un numero pronico es aquel que es generado por el producto de dos naturales consecutivos, esto es: n (n + 1) que puede ser expresado como n² + n.

  Args:
      n (int): Numero entero dado

  Returns:
      [Bool]: True si es pronico, False si no es pronico
  """

  for x in range(1, n):
      if (x**2 + x) == n:
          return True
  return False

def registro(pilotos):
  """Funcion para registrar (guardar) pilotos en nuestro programa

  Args:
      pilotos ([list]): Lista de diccionarios donde cada diccionario representa un piloto con su informacion

  Raises:
      Exception: Las cedula y horas deben ser enteras y el tipo de avion debe ser o 'j' o 'h'
  """

  # Inicio del registro por teclado
  while True:
      try:
          cedula = int(input("Ingrese su cedula: "))
          horas = int(input("Ingrese su horas: "))
          tipo_avion = input("Ingrese su tipo_avion (J)et o (H)elice: ").lower()
          if tipo_avion != 'h' and tipo_avion != 'j':
              print('Ingresa una opcion valida')
              raise Exception
          break
      except:
          print('Error')

  # Calculo del monto
  if tipo_avion == 'h':
      monto = 40 * horas
  else:
      monto = 50 * horas

  # Calculos del aumento & descuento del monto
  aumento = False
  if horas > 8:
      monto = monto * 1.10
      aumento = True

  descuento = False
  if es_pronico(cedula):
      monto = monto * .50
      descuento = True

  # Guardamos el piloto en el diccionario
  piloto = {}
  piloto['cedula'] = cedula
  piloto['horas'] = horas
  piloto['tipo_avion'] = tipo_avion
  piloto['monto'] = monto
  piloto['aumento'] = aumento
  piloto['descuento'] = descuento

  # Guardamos el piloto en la lista
  pilotos.append(piloto)

def ver_pilotos(pilotos):
  """Funcion para ver los pilotos con su informacion

  Args:
      pilotos (list):Lista de diccionarios donde cada diccionario representa un piloto con su informacion
  """
  print(f"\nLa cantidad de pilotos es: {len(pilotos)} y son:")
  for piloto in pilotos:
      print(f''' \n
          cedula: {piloto['cedula']}
          horas:{piloto['horas']}
          tipo_avion:{piloto['tipo_avion']}
          monto: ${piloto['monto']}
          aumento: {piloto['aumento']}
          descuento: {piloto['descuento']}
      ''')

def cp_por_tipo_avion(pilotos):
  """Muestra a la cantidad de pilotos por tipo de avion

  Args:
      pilotos (list):Lista de diccionarios donde cada diccionario representa un piloto con su informacion
  """
  cantidad_jet = list(filter(lambda p: p['tipo_avion'] == 'j', pilotos))

  cantidad_helice = list(filter(lambda p: p['tipo_avion'] == 'h', pilotos))

  print(f'Cantidad de pilotos en Jet {len(cantidad_jet)}')

  print(f'Cantidad de pilotos en Helice {len(cantidad_helice)}')

def cp_por_aumento_descuento(pilotos):
  """Muestra la cantidad de pilotos que se le ha aplicado algun aumento/descuento

  Args:
    pilotos (list):Lista de diccionarios donde cada diccionario representa un piloto con su informacion
  """
  cantidad_aumento = list(filter(lambda p: p['descuento'], pilotos))

  cantidad_descuento = list(filter(lambda p: p['aumento'], pilotos))

  print(f'Cantidad de pilotos con aumento {len(cantidad_aumento)}')

  print(f'Cantidad de pilotos con descuento {len(cantidad_descuento)}')

def promedio_de_pagos(pilotos):
  """ Calcula el promedio de pagos de los pilotos por tipo de avion, Helice o Jet

  Args:
      pilotos (list):Lista de diccionarios donde cada diccionario representa un piloto con su informacion
  """

  cantidad_jet = list(filter(lambda p: p['tipo_avion'] == 'j', pilotos))

  cantidad_helice = list(filter(lambda p: p['tipo_avion'] == 'h', pilotos))

  monto_jet = [piloto['monto'] for piloto in cantidad_jet]

  if len(monto_jet)  == 0:
    promedio_jet = 0
    print("\nNo hay pilotos con tipo de avion Jet registrados")
  else:
    promedio_jet = sum(monto_jet)/len(monto_jet)

  monto_helice = [piloto['monto'] for piloto in cantidad_helice]

  if len(monto_helice) == 0:
    promedio_helice = 0
    print("No hay pilotos con tipo de avion Helice registrados\n")
  else:
    promedio_helice = sum(monto_helice)/len(monto_helice)

  print(f'Promedio en Jet ${promedio_jet}')

  print(f'Promedio en Helice ${promedio_helice}')

def main():
  """Funcion de inicio del programa, inicializamos nuestra base de datos de pilotos, una lista de diccionarios, donde cada diccionario es un piloto, y mostramos el menu con las diferentes opciones del programa
  """
  pilotos = [
              {
                  "cedula": 1234,
                  "horas": 2,
                  "tipo_avion": 'j',
                  "monto": 100,
                    "aumento": False,
                  "descuento": False,
              },{
                  "cedula": 31231,
                  "horas": 1,
                  "tipo_avion": 'h',
                  "monto": 40,
                  "aumento": True,
                  "descuento": True,
              },
          ]

  # pilotos = []

  while True:
      opcion = input('''
          Bienvenido a Saman Airlines
          1. Registro
          2. C.P con su info
          3. C.P por tipo de avion
          4. C.P. por descuento/aumento
          5. Promedio de pago por tipo de avion
          6. Salir
      > ''')
      if opcion == '1':
          registro(pilotos)
          ver_pilotos(pilotos)
      elif opcion == '2':
          ver_pilotos(pilotos)
      elif opcion == '3':
          cp_por_tipo_avion(pilotos)
      elif opcion == '4':
          cp_por_aumento_descuento(pilotos)
      elif opcion == '5':
          promedio_de_pagos(pilotos)
      else:
          print("Adios!")
          break

main()
