"""
	Funciones Puras
	Efectos secundarios
	@pablom7
"""
import csv
# Usamos una funcion para leer el archivo 
def lineas(archivo):
	return csv.reader(archivo, delimiter= ";")
# Usamos una funcion para manejar el archivo
with open("data/data-estudiantes.csv") as midata:
# Presentamos el archivo
	print(list(lineas(midata)))

# midata = open("data/data-estudiantes.csv") # en usos de grander volumenes de \
		# datos es necesario cerrar el archivo
# print(list(lineas(midata)))
# midata.close() 