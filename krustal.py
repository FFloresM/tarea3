import grafo
import ListaLigada
import sys

def leer_grafo(file):
	g = set()
	with open(file, 'r') as file:
		content = file.read().splitlines()
	for i in content:
		g.add(tuple(int(x) for x in i.split()))
	return g
#print(sys.argv)
try:
	archivo = sys.argv[1]
	
except IndexError:
	print("ingrese nombre archivo: \n$ python3.x krustal.py nombre_archivo")
	exit()

g = leer_grafo(archivo)
grafo = grafo.Grafo(g)
print(grafo.conj)
"""
print(grafo.Vertices())
print(grafo.Aristas())
"""