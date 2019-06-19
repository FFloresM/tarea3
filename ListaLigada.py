class Nodo():
	"""Clase nodo"""
	def __init__(self, dato):
		self.dato = dato
		self.sig = None

	def getDato(self):
		return self.dato

	def getSig(self):
		return self.sig

	def setDato(self, newdato):
		self.dato = newdato

	def setSig(self, newsig):
		self.sig = newsig

class ListaLigada(object):
	"""docstring for ListaLigada"""
	def __init__(self):
		self.head = head

	def isEmpty(self):
		return self.head == None

	def agregar(self, item):
		temp = Nodo(item)
		temp.setSig(self.head)
		self.head = temp

	def size(self):
		actual = self.head
		count = 0
		while actual != None:
			count +=1
			actual = actual.getSig()
		return count

	def buscar(self, item):
		actual = self.head
		found = False
		while actual != None and not found:
			if actual.getDato == item:
				found = True
			else:
				actual = actual.getSig()
		return found

	def eliminar(self, item):
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
