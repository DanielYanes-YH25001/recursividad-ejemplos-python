def contar_elemento(estructura, objetivo):
  contador = 0

  # Caso base, la recursión finalizará cuando no haya más elementos a recorrer
  for elemento in estructura:
    # Realizamos recursión solamente si el elemento es una lista
    if isinstance(elemento, list):
      contador += contar_elemento(elemento, objetivo)
    elif elemento == objetivo:
      # Caso base cuando el elemento sea lo que buscamos
      contador += 1

  # Finalmente retornamos el contador de apariciones
  return contador

# Contamos cuantas veces aparece el número 1 en la lista anidada "datos"
datos = [1, [2, 1, [1, 3]], 1, [4, [1]]]
print(contar_elemento(datos, 1))