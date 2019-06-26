class Grafo:
	"""Clase para representar Grafo no dirigido con pesos"""
	def __init__(self, conj=None):
		"""conj: conjunto de aristas representadas como (a,b,p).
			(a,b) en E (conjunto de aristas) y p = peso arista (a,b)"""
		if conj is None:
			self.conj = []
		self.conj = conj
		self.vertices = None
		self.aristas = None

	def Vertices(self):
		"""Devuelve el conjunto de vertices V"""
		v = []
		for i in self.conj:
			v.append(i[0])
			v.append(i[1])
		self.vertices = set(v)
		return list(self.vertices)

	def AddEdge(self,tupla):
		"""Agregar una arista (a,b,p) con vertices a, b y peso p"""
		if len(tupla) == 3:
			self.conj.append(tupla)
		else:
			print("largo de tupla debe ser 3")

	def Aristas(self):
		"""Devuelve el conjunto de aristas E"""
		edges = {}
		for i in self.conj:
			edges[(i[0],i[1])] = i[2]
		self.aristas = edges
		return list(self.aristas.keys())

	def peso(self, ar):
		"""Devueve el peso de una arista ar ingresada como par (u,v) en E"""
		if ar in self.aristas:
			return self.aristas[ar]

	def sort(self):
		"""ordena las aristas por peso"""
		self.conj = sorted(self.conj, key = lambda peso: peso[2])