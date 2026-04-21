import os

def buscar_archivo(ruta, nombre_buscado):
  # Recorremos cada elemento de la carpeta donde se buscará
  for elemento in os.listdir(ruta):
    ruta_completa = os.path.join(ruta, elemento)

    # En caso el elemento sea un archivo
    if os.path.isfile(ruta_completa):
      if elemento == nombre_buscado:
        # Retornamos la ruta completa del archivo si lo encontramos
        return ruta_completa
    else:
      # En caso el elemento no sea un archivo, si no que sea una carpeta,
      # continuamos buscando en dicha carpeta de forma recursiva
      resultado = buscar_archivo(ruta_completa, nombre_buscado)
      if resultado:
        return resultado

  # Finalmente retornamos None en caso el archivo no sea encontrado    
  return None

# Probar la función de la siguiente manera:
# print(buscar_archivo('COLOCAR AQUÍ LA RUTA DE LA CARPETA DONDE SE BUSCARÁ', 'COLOCAR AQUÍ EL NOMBRE DEL ARCHIVO INCLUYENDO SU EXTENSIÓN'))