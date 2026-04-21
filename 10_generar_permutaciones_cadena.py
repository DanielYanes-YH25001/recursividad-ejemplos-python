def obtener_permutaciones(cadena):
  # Caso base, cuando la cadena contenga un solo carácter,
  # o en caso la cadena este vacía
  if len(cadena) <= 1:
    return [cadena]
  
  resultado = []

  for i, letra in enumerate(cadena):
    # Quitamos la letra actual
    resto = cadena[:i] + cadena[i + 1:]

    # Permutamos el resto de letras de forma recursiva
    for p in obtener_permutaciones(resto):
      resultado.append(letra + p)

  # Finalmente retornamos el resultado  
  return resultado

print(obtener_permutaciones("abc"))
print(obtener_permutaciones("hola"))