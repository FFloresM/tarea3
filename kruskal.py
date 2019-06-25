import grafo
import ListaLigada
from Union_find import List_Set, List_Set_T
import sys

def leer_grafo(file):
	g = set()
	with open(file, 'r') as file:
		content = file.read().splitlines()
	for i in content:
		g.add(tuple(int(x) if x.isdigit() else x for x in i.split()))
	return g

try:
	archivo = sys.argv[1]	
except IndexError:
	print("ingrese nombre archivo: \n$ python3.x krustal.py nombre_archivo")
	exit()

try:
	modo = sys.argv[2]
except IndexError:
	print("ingrese modo: \n$ python3.x krustal.py nombre_archivo modo")
	exit()


g = leer_grafo(archivo)
grafo = grafo.Grafo(g)

if modo == 'arbol':
	lst = List_Set_T()
elif modo == 'listah':
	lst = List_Set(1)
elif modo == 'lista':
	lst = List_Set()
else:
	print("modo no válido")
	exit()

#Krustal
A = set()
ES = grafo.Aristas()
for v in grafo.Vertices():
	lst.makeSet(v)

for u,v in ES:
	if lst.find(u) != lst.find(v):
		A.add((u,v))
		lst.union(u, v)
##
print('T:', A)
w = 0
for i in A:
	w += grafo.peso(i)
print('w(T) = ',w)


