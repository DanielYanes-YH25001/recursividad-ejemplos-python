# Obtener el MCD (Máximo Común Divisor) entre dos números
# enteros cualesquiera, utilizando el algoritmo Euclidiano

def mcd(a, b):
  # Caso base, si alguno de los dos números es cero, el
  # MCD siempre será el otro número distinto de cero
  if b == 0:
    return a
  
  # Retornamos de forma recursiva el MCD
  return mcd(b, a % b)

print(mcd(0, 2))
print(mcd(24, 36))
print(mcd(36, 5))
print(mcd(125, 765))