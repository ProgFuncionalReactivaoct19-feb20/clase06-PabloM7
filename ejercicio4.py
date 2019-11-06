"""
	
	@pablom7
"""
import csv
# Usamos una funcion para leer el archivo 
def lineas(archivo):
	return csv.reader(archivo, delimiter= ";")
# Usamos una funcion para abrir el archivo
with open("data/data-estudiantes.csv") as midata:
# Usamos la funcion map para iterar entre los archivos y filter para obtener los datos deseados
	print(list(map(lambda x: x[1], filter(lambda x: x[1] != "email", lineas(midata)))))
