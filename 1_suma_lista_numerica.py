def suma_lista(lista):
  # Caso base, cuando la lista este vacía
  if not lista:
    return 0
  
  # Retornamos la suma del primer elemento de la lista con los siguientes
  return lista[0] + suma_lista(lista[1:])

print(suma_lista([1, 4, 7, 2]))
print(suma_lista([8273, 236, 772, 2682]))
print(suma_lista([1923, 45, 881, 345]))