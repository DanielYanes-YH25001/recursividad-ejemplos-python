 #clases y definición 
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def profundidad(nodo):
    if nodo is None:  # Caso base: árbol vacío
        return 0
    else:
        # Caso recursivo: 1 + máximo entre la profundidad del hijo izquierdo y derecho
        return 1 + max(profundidad(nodo.izq), profundidad(nodo.der))

# Construcción de un árbol
raiz = Nodo(1)
raiz.izq = Nodo(2)
raiz.der = Nodo(3)
raiz.izq.izq = Nodo(4)
raiz.izq.der = Nodo(5)

print(profundidad(raiz))  # Salida: 3
