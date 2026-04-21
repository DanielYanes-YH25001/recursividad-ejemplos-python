def serie_fibonacci(numero_secuencia):
  # Caso base, cuando el número de la secuencia sea cero o uno
  if numero_secuencia <= 1:
    return numero_secuencia

  # Retornamos la suma de los dos números anteriores
  return serie_fibonacci(numero_secuencia - 1) + serie_fibonacci(numero_secuencia - 2)

# Ahora podemos mostrar n elementos de la secuencia de
# fibonacci. En este ejemplo se muestran los primeros 10
for i in range(10):
  print(serie_fibonacci(i))