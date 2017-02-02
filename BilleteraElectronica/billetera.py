class Billetera():
	def __init__(self, id, nombre, apellidos, ci, pin):
		self.id = id
		self.nombres = nombre
		self.apellidos = apellidos
		if (type(ci) != int):
			return False
		else:
			self.ci = ci
		self.pin = pin
		self.creditos = []
		self.debitos = []

	def mostrar(self):
		print('La billetera es de {} {}'.format(self.nombres,self.apellidos))
		s = 'Su ci es '+ repr(self.ci) +' y el pin es ' + repr(self.pin) + '.\n'
		print(s)

	def mostrarC(self):
		for i in range(0,len(self.creditos)):
			aux = self.creditos[i]
			s = repr(aux.id)+':\tConsumo del ' + aux.fecha + ' por un monto de ' + repr(aux.monto)
			print(s)

	def saldo(self):
		c = 0 
		d = 0
		for i in range(0,len(self.creditos)):
			c = c + self.creditos[i].monto
		for i in range(0,len(self.debitos)):
			d = d + self.debitos[i].monto
		return c-d

	def recargar(self, monto, fecha, id):
		if (monto <= 0):
			print("El monto a recargar no puede ser menor o igual a cero")
			return False
		else:
			aux = Cargas(monto,fecha,id)
			self.creditos.append(aux)
			return True

	def consumir(self, monto, fecha, id, pin):

		if (monto <= 0):
			print("El monto a consumir no puede ser menor o igual a cero")
			return False
		else:
			if (self.saldo() >= monto) and (pin == self.pin):
				aux = Cargas(monto,fecha,id)
				self.debitos.append(aux)
				return True
			else:
				if self.saldo() < monto:
					print("Saldo insuficiente")
					return False
				else:
					print("El pin ingresado es incorrecto")
					return False


class Cargas:
	def __init__(self,monto = 0,fecha='',id=0):
		self.monto = monto #Debe ser mayor estricto que cero
		self.fecha = fecha
		self.id = id
