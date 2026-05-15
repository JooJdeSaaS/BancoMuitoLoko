from abc import ABC, abstractmethod

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Conta:
    def __init__(self, cliente, saldo, historico=None):
        self.cliente = cliente
        self.saldo = saldo
        self.numero_conta = f"001-{cliente.cpf[-3:]}"
        self.historico = historico if historico else [f"Abertura: R$ {saldo:.2f}"]

class IContaRepository(ABC):
    @abstractmethod
    def salvar(self, conta: Conta):
        pass

    @abstractmethod
    def buscar_por_cpf(self, cpf: str) -> Conta:
        pass