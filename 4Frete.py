from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def calcular(self, distancia):
        pass

class Moto(Transporte):
    def calcular(self, distancia):
        return distancia * 2.0

class Carro(Transporte):
    def calcular(self, distancia):
        return (distancia * 3.5) + 10.0

class Caminhao(Transporte):
    def calcular(self, distancia):
        return (distancia * 8.0) + 50.0

class Bicicleta(Transporte):
    def calcular(self, distancia):
        return distancia * 1.0

class CalculadoraDeFrete:
    def calcular_frete(self, transporte: Transporte, distancia):
        if not isinstance(transporte, Transporte):
            raise ValueError("Tipo de transporte desconhecido")
        return transporte.calcular(distancia)