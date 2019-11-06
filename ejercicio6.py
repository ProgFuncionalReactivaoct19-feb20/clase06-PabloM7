"""
	@pablom7
"""
import csv

# Usamos una funcion para leer el archivo
def lineas(archivo):
	return csv.DictReader(archivo, delimiter= "\t")

# Usamos una funcion para abrir el archivo
with open("data/trabajadores.csv") as midata:
# Transformamos el archivo en una lista
	lista_trabajadores = list(lineas(midata))
# Presentamos las lineas cuya longitud es mayor a 10
	print(list(filter(lambda x: len(list(x.items())[2][1] > 10, lista_trabajadores))))
# Ordenamos y presentamos las listas segun el dia de nacimiento	
	print(sorted(lista_trabajadores, key = lambda x: list(x.items())[1][1].split("-")[2]))