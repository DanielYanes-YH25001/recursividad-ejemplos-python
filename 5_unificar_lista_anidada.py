def unificar(lista):
  resultado = []
  
  # Caso base, la recursión finalizará cuando no haya más elementos a recorrer
  for elemento in lista:
    # Si el elemento actual es una lista la unificamos recursivamente
    if isinstance(elemento, list):
      resultado += unificar(elemento)
    else:
      # Si el elemento actual no es una lista, simplemente
      # lo agregamos a la lista a retornar
      resultado.append(elemento)
  
  # Retornamos la lista unificada
  return resultado

# Vamos a obtener una única lista con el contenido de las listas anidadas
print(unificar([1, [2, 3], [4, [5, 6]]]))
print(unificar([76, [23, 24], [87, [ 77, 9, [15, 22]]]]))