from ListaLigada import Nodo, ListaLigada

class List_Set:
	"""docstring for List_Set"""
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
		xRaiz = self.find(x)
		yRaiz = self.find(y)
		if(xRaiz == yRaiz):
			return
		if self.rank[xRaiz] < self.rank[yRaiz]:
			self.padre[xRaiz] = yRaiz
		elif self.rank[xRaiz] > self.rank[yRaiz]:
			self.padre[yRaiz] = xRaiz
		else:
			self.padre[yRaiz] = xRaiz
			self.rank[xRaiz]+=1
		
	




		




		