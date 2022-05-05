from unittest import TestCase
from hoteis import Hoteis

class Tests(TestCase):
    def test_cliente(self):
        assert Hoteis.getTipoCliente == "Regular" or "Reward" 
        
    def test_dataEntrada(self):
        assert Hoteis.getDataEntrada == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20 or 21 or 22 or 23 or 24 or 25 or 26 or 27 or 28 or 29 or 30 or 31
        
    def test_dataSaida(self):
        assert Hoteis.getDataSaida == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20 or 21 or 22 or 23 or 24 or 25 or 26 or 27 or 28 or 29 or 30 or 31
        
    def test_valoresHoteis(self):
        assert Hoteis.valoresHoteis == {'Lakewood': 3} or {' Bridgewood': 4} or {' Ridgewood': 5}
        