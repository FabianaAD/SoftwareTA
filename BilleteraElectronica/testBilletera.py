'''
Created on 2 feb. 2017

@author: Gabriel Torres 13-11412
         Fabiana Acosta 10-10005
'''
import unittest
from billetera import *

class Test(unittest.TestCase):

    # Inicializacion de la clase Billetera
    def setUp(self):
        Id = 1
        Nombre = "Gabriel"
        Apellido = "Torres"
        CI = 24218683
        Pin = 0001
        self.B = Billetera(Id, Nombre, Apellido, CI, Pin)

    # Prueba de recarga negativa
    def test1(self):
        monto = -15
        self.assertEquals(False, self.B.recargar(monto, '31/1/2017', 24218683))

    # Prueba de recarga igual a 0
    def test2(self):
        monto = 0
        self.assertEquals(False, self.B.recargar(monto, '31/1/2017', 24218683))
        
    #Prueba de al recargar 1500, existan 1500 de saldo    
    def test3(self):
        monto = 1500
        self.B.recargar(monto, '31/1/2017', 24218683)
        self.assertEquals(True, self.B.saldo() == 1500)
        
    # Prueba de consumir un monto igual a 0    
    def test4(self):
        monto = 0
        self.assertEquals(False, self.B.consumir(monto, '31/1/2017', 24218683, 0001))
    
    # Prueba que verifica si al recargar 1500 y se consumen 1000, queda en saldo 500
    def test5(self):
        monto = 1500
        self.B.recargar(monto, '31/1/2017', 24218683)
        monto1 = 1000
        self.B.consumir(monto1, '31/1/2017', 24218683, 0001)
        self.assertEquals(True, self.B.saldo() == 500)
    
    # Prueba de tener saldo de 1500, hacer un consumo negativo igual a -10    
    def test6(self):
        monto = 1500
        self.B.recargar(monto, '31/1/2017', 24218683)
        monto1 = -10
        self.assertEquals(False, self.B.consumir(monto1, '31/1/2017', 24218683, 0001))
    
    # Prueba de recargar 1500 y consumir 1500, que quede 0 en saldo
    def test7(self):
        monto = 1500
        self.B.recargar(monto, '31/1/2017', 24218683)
        monto1 = 1500
        self.B.consumir(monto1, '31/1/2017', 24218683, 0001)
        self.assertEquals(True, self.B.saldo() == 0)
    
    # Prueba de recargar 1500 y consumir 1499, que quede 1 en saldo    
    def test8(self):
        monto = 1500
        self.B.recargar(monto, '31/1/2017', 24218683)
        monto1 = 1499
        self.B.consumir(monto1, '31/1/2017', 24218683, 0001)
        self.assertEquals(True, self.B.saldo() == 1)
    
    # Prueba de recargar un monto muy alto
    def test9(self):
        monto = float('inf')
        self.B.recargar(monto, '31/1/2017', 24218683)
        self.assertEquals(True, self.B.saldo() == float('inf'))
    
    # Prueba de consumir 1499 cuando hay 0 en saldo    
    def test10(self):
        monto1 = 1499
        self.assertEquals(True, self.B.saldo() == 0)
        self.assertEquals(False, self.B.consumir(monto1, '31/1/2017', 24218683, 0001))
        
    # Prueba de hacer un consumo con un pin disferente al de la persona duenna de la billetera
    def test11(self):
        monto = 1500
        self.B.recargar(monto, '31/1/2017', 24218683)
        monto1 = 50
        self.assertEquals(False, self.B.consumir(monto1, '31/1/2017', 24218683, 0002))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()