from ListaLigada import Nodo, ListaLigada

class List_Set:
	"""Estructura Union-Find usando listas ligadas"""
	def __init__(self, h=None):
		"""si h entonces se hace merge con heuristica """
		self.nodoDir = dict()
		self.new_set = None
		self.h = h

	def makeSet(self, x):
		""" Crea un nuevo conjunto con unico elelemto x"""
		self.new_set = ListaLigada()
		self.new_set.head = Nodo()
		self.new_set.tail = self.new_set.head
		self.nodoDir[x] = self.new_set.head
		self.new_set.head.setDato(x)
		self.new_set.head.l_head = self.new_set


	def union(self, x, y):
		"""Union de x e y. Si h, entonces la lista con menos elementos se agrega al final de la mas larga """
		s_x = self.find(x)
		s_y = self.find(y)
		
		ls_x = s_x.size()
		ls_y = s_y.size()

		if self.h and ls_x > ls_y:
			self.unionh(s_x, s_y)
		else:
			self.unionh(s_y,s_x)	

	def unionh(self, l1, l2):
		"""Une l2 a l1, elimina l2"""
		act = l2.head
		while act:
			act.l_head = l1
			act = act.getSig()
		l1.tail.sig = l2.head
		l1.tail = l2.tail
		del l2

	def find(self, x):
		"""Busca x en en la coleccion de conjuntos y retorna un puntero a su representante"""
		nodo = self.nodoDir[x]
		return nodo.l_head

	def findv(self, x):
		""" Busca x en en la coleccion de conjuntos y retorna su representante """
		nodo = self.nodoDir[x]
		return nodo.l_head.head.dato

class List_Set_T(object):
	""" Estructura Union-Find usando bosque de arboles """
	def __init__(self):
		self.padre = dict()
		self.rank = dict()

	def makeSet(self,x):
		""" Crea un nuevo conjunto con unico elelemto x"""
		self.padre[x] = x
		self.rank[x] = 0

	def find(self, x):
		"""Busca x en en la coleccion de conjuntos y retorna su representante"""
		if(self.padre[x]!=x):
			self.padre[x]=self.find(self.padre[x])
		return self.padre[x]

	def union(self, x, y):
		""" Busca los representantes de x e y y llama a link"""
		x_raiz = self.find(x)
		y_raiz = self.find(y)
		self.link(x_raiz, y_raiz)
		

	def link(self, x, y):
		""" La raiz de menor rank se hace apuntar a la de mayor rank """
		if(x == y):
			return
		if self.rank[x] < self.rank[y]:
			self.padre[x] = y
		elif self.rank[x] > self.rank[y]:
			self.padre[y] = x
		else:
			self.padre[y] = x
			self.rank[x]+=1
