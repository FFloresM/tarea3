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
archivo = sys.argv[1]
g = leer_grafo(archivo)
grafo = grafo.Grafo(g)
print(grafo.Vertices())
print(grafo.Aristas())