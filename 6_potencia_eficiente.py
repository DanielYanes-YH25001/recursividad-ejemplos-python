def potencia_eficiente(base, exponente):
  # Caso base, si el exponente es cero retornamos uno
  if exponente == 0:
    return 1

  # Si el exponente es un número par, calculamos la potencia
  # utilizando la mitad del exponente de forma recursiva
  if exponente % 2 == 0:
    mitad = potencia_eficiente(base, exponente / 2)

    # Retornamos el producto de las dos potencias calculadas con la mitad del exponente
    return mitad * mitad
  else:
    # En caso el exponente sea un número impar, calculamos la potencia
    # utilizando un número menos que el exponente y retornamos el producto
    # de la base y la potencia anteriormente calculada de forma recursiva
    return base * potencia_eficiente(base, exponente - 1)
  
print(potencia_eficiente(2, 3))
print(potencia_eficiente(3, 10))
print(potencia_eficiente(10, 3))
print(potencia_eficiente(2, 32))