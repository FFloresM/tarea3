from ListaLigada import Nodo, ListaLigada

class List_Set:
	"""docstring for List_Set"""
	def __init__(self):
		self.nodoDir = dict()
		self.new_set = None

	def makeSet(self, x):
		self.new_set = ListaLigada()
		temp = Nodo(x)
		self.new_set.head = temp
		self.new_set.tail = self.new_set.head
		self.nodoDir[x] = self.new_set.head
		temp.l_head = self.new_set

		return self.new_set

	def union(self, l1, l2):
		act = l2.head 
		while act.getSig():
			act.l_head = l1
			act = act.getSig()
		l1.tail.sig = l2.head
		l1.tail = l2.tail
		del l2

	def find(self, x):
		nodo = self.nodoDir[x]
		return nodo.l_head

class List_Set_T(object):
	"""docstring for List_Set_T"""
	def __init__(self):
		self.padre = dict()
		self.rank = dict()

	def makeSet(self,x):
		self.padre[x] = x
		self.rank[x] = 0

	def Buscar(self, x):
		if(self.padre[x]!=x):
			self.padre[x]=self.Buscar(self.padre[x])
		return self.padre[x]

	def Union(self, x, y):
		xRaiz = self.Buscar(x)
		yRaiz = self.Buscar(y)
		if(xRaiz == yRaiz):
			return
		if self.rank[xRaiz] < self.rank[yRaiz]:
			self.padre[xRaiz] = yRaiz
		elif self.rank[xRaiz] > self.rank[yRaiz]:
			self.padre[yRaiz] = xRaiz
		else:
			self.padre[yRaiz] = xRaiz
			self.rank[xRaiz]+=1
		
	




		




		