def invertir(cadena):
  # Caso base, cuando la cadena contenga un solo carácter
  # o en caso la cadena este vacía
  if len(cadena) <= 1:
    return cadena
  
  # Retornamos la concatenación del último carácter de la cadena con los anteriores
  return cadena[-1] + invertir(cadena[:-1])

print(invertir("hola"))
print(invertir("programación"))
print(invertir("python"))
print(invertir("2026"))
print(invertir(""))