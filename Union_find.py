from ListaLigada import Nodo, ListaLigada

class List_Set:
	"""Estructura Union-Find usando listas ligadas"""
	def __init__(self):
		self.nodoDir = dict()
		self.new_set = None

	def makeSet(self, x):
		self.new_set = ListaLigada()
		self.new_set.head = Nodo()
		self.new_set.tail = self.new_set.head
		self.nodoDir[x] = self.new_set.head
		self.new_set.head.setDato(x)
		self.new_set.head.l_head = self.new_set


	def union(self, x, y):
		s_x = self.find(x)
		s_y = self.find(y)
		act = s_y.head
		while act:
			act.l_head = s_x
			act = act.getSig()
		s_x.tail.sig = s_y.head
		s_x.tail = s_y.tail
		del s_y

	def find(self, x):
		nodo = self.nodoDir[x]
		return nodo.l_head

	def findv(self, x):
		nodo = self.nodoDir[x]
		return nodo.l_head.head.dato

class List_Set_T(object):
	"""docstring for List_Set_T"""
	def __init__(self):
		self.padre = dict()
		self.rank = dict()

	def makeSet(self,x):
		self.padre[x] = x
		self.rank[x] = 0

	def find(self, x):
		if(self.padre[x]!=x):
			self.padre[x]=self.find(self.padre[x])
		return self.padre[x]

	def union(self, x, y):
		x_raiz = self.find(x)
		y_raiz = self.find(y)
		self.link(x_raiz, y_raiz)
		

	def link(self, x, y):
		if(x == y):
			return
		if self.rank[x] < self.rank[y]:
			self.padre[x] = y
		elif self.rank[x] > self.rank[y]:
			self.padre[y] = x
		else:
			self.padre[y] = x
			self.rank[x]+=1

		
	




		




		