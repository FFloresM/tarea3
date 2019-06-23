class Grafo:
	"""Grafo con pesos"""
	def __init__(self, conj=None):
		"""conj: conjunto de aristas representadas como (a,b,p) ordenadas por peso.
			(a,b) en E (conjunto de aristas) y p = peso arista (a,b)"""
		if conj is None:
			self.conj = set()
		self.conj = sorted(conj, key = lambda peso: peso[2])
		self.vertices = None
		self.aristas = None

	def Vertices(self):
		"""Devuelve el conjunto de vértices V"""
		v = []
		for i in self.conj:
			v.append(i[0])
			v.append(i[1])
		self.vertices = set(v)
		return list(self.vertices)

	def AddEdge(self,tupla):
		"""Agregar una arista (a,b,p) con vertices a, b y peso p"""
		if len(tupla) == 3:
			self.conj.add(tupla)
		else:
			print("largo de tupla debe ser 3")

	def Aristas(self):
		"""Devuelve el conjunto de aristas E"""
		edges = []
		for i in self.conj:
			edges.append((i[0],i[1]))
		self.aristas = set(edges)
		return self.aristas