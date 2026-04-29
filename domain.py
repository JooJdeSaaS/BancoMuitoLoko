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

    def aplicar_rendimento(self, taxa: float):
        rendimento = self.saldo * taxa
        self.saldo += rendimento
        self.historico.append(f"Rendimento Poupança: + R$ {rendimento:.2f}")
        return rendimento

    def investir_poupanca(self, cpf, taxa=0.005):  # Define 0.5% como padrão
        conta = self.repository.buscar_por_cpf(cpf)
        if conta:
            rendimento = conta.aplicar_rendimento(taxa)
            self.repository.salvar(conta)
            return True, f"Rendimento de R$ {rendimento:.2f} aplicado!"
        return False, "Conta não encontrada."

class IContaRepository(ABC):
    @abstractmethod
    def salvar(self, conta: Conta):
        pass

    @abstractmethod
    def buscar_por_cpf(self, cpf: str) -> Conta:
        pass