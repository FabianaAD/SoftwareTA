class Billetera:
	def __init__(self,id,nombre,apellidos,ci,pin):
		self.id = id
		self.nombres = nombre
		self.apellidos = apellidos
		if type(ci) != int:
    		raise TypeError, "i debe ser del tipo int"
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

	def recargar(self,monto,fecha,id):
		if (monto<=0):
			print("El monto a recargar no puede ser menor o igual a cero")
		else:
			aux = Cargas(monto,fecha,id)
			self.creditos.append(aux)

	def consumir(self,monto,fecha,id,pin):

		if (monto<=0):
			print("El monto a consumir no puede ser menor o igual a cero")
		else:
			if (self.saldo()>=monto) and (pin ==self.pin):
				aux = Cargas(monto,fecha,id)
				self.debitos.append(aux)
			else:
				if self.saldo()<monto:
					print("Saldo insuficiente")
				else:
					print("El pin ingresado es incorrecto")


class Cargas:
	def __init__(self,monto = 0,fecha='',id=0):
		self.monto = monto #Debe ser mayor estricto que cero
		self.fecha = fecha
		self.id = id


B = Billetera('blue','Fabiana José','Acosta Díaz',24401656,1234)
B.mostrar()

B.mostrarC()
B.recargar(-1500,'31/1/2017',24401)
B.mostrarC()
B.recargar(1500,'31/1/2017',2445)
s = 'El saldo es ' + repr(B.saldo())
print(s)
B.consumir(-6500,'31/1/2017',24408,1234)
s = 'El saldo es ' + repr(B.saldo())
print(s)
B.recargar(10500,'31/1/2017',2401)
B.consumir(500,'31/1/2017',2441,1237)
B.consumir(3600,'31/1/17',22214,1234)
s = 'El saldo es ' + repr(B.saldo())
print(s)
B.mostrarC()
