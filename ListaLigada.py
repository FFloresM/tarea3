class Nodo:
	"""Clase nodo"""
	def __init__(self, dato=None):
		"""Nodo con dato, puntero al siguiente elemento y puntero a su lista"""
		self.dato = dato
		self.sig = None
		self.l_head = None

	def getDato(self):
		""" obtener dato"""
		return self.dato

	def getSig(self):
		""" obtener nodo siguiente"""
		return self.sig

	def setDato(self, newdato):
		"""Asignar dato"""
		self.dato = newdato

	def setSig(self, newsig):
		"""Asignar elemento siguiente"""
		self.sig = newsig


class ListaLigada(object):
	"""docstring for ListaLigada"""
	def __init__(self):
		"""Crea nueva lista con puntero al inicio y al final"""
		self.head = None
		self.tail = None

	def isEmpty(self):
		""" retorna True si la lista esta vacia y False si no"""
		return self.head == None

	def agregar(self, item):
		"""Agrega un nuevo elemento al final de la lista"""
		temp = Nodo(item)
		if self.isEmpty():			
			self.head = temp
			self.tail = temp
		else:
			actual = self.head
			while actual.getSig():
				actual = actual.getSig()
			actual.setSig(temp)
			self.tail = actual

	def size(self):
		"""Devuelve la cantidad de elementos en la lista"""
		actual = self.head
		count = 0
		while actual != None:
			count +=1
			actual = actual.getSig()
		return count

	def buscar(self, item):
		"""Busca un elemento en la lista"""
		actual = self.head
		found = False
		while actual != None and not found:
			if actual.getDato == item:
				found = True
			else:
				actual = actual.getSig()
		return found

	def eliminar(self, item):
		"""elimina un elemento de la lista"""
		actual =self.head
		prev = None
		found = False
		while not found:
			if actual.getDato() == item:
				found = True
			else:
				prev = actual
				actual = actual.getSig()
		if prev == None:
			self.head = actual.getSig()
		else:
			prev.setSig(actual.getSig())

	def mostrar(self):
		"""muestra la lista"""
		actual = self.head
		while actual != None:
			print(actual.self.getDato(), end='')
			actual = actual.self.getSig()
			if actual != None:
				print(" ->", end=" ")
		print()