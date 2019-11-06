"""
	@pablom7
"""

import csv
# Usamos una funcion para leer el archivo 
def lineas(archivo):
	return csv.DictReader(archivo, delimiter= ";")
# Usamos una funcion para abrir el archivo
with open("data/data-estudiantes.csv") as midata:
# Transformamos el archivo en una lista
	convertir = list(lineas(midata))
# Usamos la funcion map para iterar entre los elementos de la lista y usamos la funcion split para separar la parte del texto que se desea
	print(list(map(lambda x: "%s %s" %(list(x.items())[0][1].split(" ")[1], list(x.items())[1][1].split(".")[0]), convertir)))
