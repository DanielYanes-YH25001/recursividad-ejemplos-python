def caballo_puede_llegar(x1, y1, x2, y2, k):
  # Los 8 movimientos posibles del caballo
  movimientos = [
    (2, 1),
    (2, -1),
    (-2, 1),
    (-2, -1),
    (1, 2),
    (1, -2),
    (-1, 2),
    (-1, -2),
  ]

  # Primer caso base, cuando los movimientos son de más
  if k < 0:
    return False
  
  # Segundo caso base, cuando el caballo llegó justo en k movimientos
  if x1 == x2 and y1 == y2:
    return k == 0

  # Caso recursivo, cuando el caballo realiza sus 8 movimientos
  for dx, dy in movimientos:
    nuevo_x, nuevo_y = x1 + dx, y1 + dy

    # Verificamos si el nuevo movimiento del caballo cae dentro del tablero de 8x8
    if 0 <= nuevo_x < 8 and 0 <= nuevo_y < 8:
      if caballo_puede_llegar(nuevo_x, nuevo_y, x2, y2, k - 1):
        return True

  # En caso los movimientos no alcancen    
  return False

# Probamos si un caballo puede ir de la casilla a1 a b3
# en 1 movimiento, siendo a1 = 0,0 y b3 = 1,2
print(caballo_puede_llegar(0, 0, 1, 2, 1))

# Probamos si un caballo puede ir de la casilla a1 a h8
# en 6 movimientos, siendo a1 = 0,0 y h8 = 7,7
print(caballo_puede_llegar(0, 0, 7, 7, 6))

# Probamos si un caballo puede ir de la casilla d4 a d8
# en 3 movimientos, siendo d4 = 3,3 y h8 = 3,7 (en este caso los movimientos son de más)
print(caballo_puede_llegar(3, 3, 3, 7, 3))

# Probamos si un caballo puede ir de la casilla f3 a f1
# en 1 movimiento, siendo f3 = 5,2 y f1 = 5,0 (en este caso los movimientos no alcanzan)
print(caballo_puede_llegar(5, 2, 5, 0, 1))