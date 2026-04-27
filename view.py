class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Conta:
    def __init__(self, cliente, saldo_inicial):
        self.cliente = cliente
        self.saldo = saldo_inicial
        # Simulação de um número de conta gerado
        self.numero_conta = "001-" + str(cpf[-3:])

class BancoDados:
    """Simulação de um banco de dados persistente em memória."""
    def __init__(self):
        self.contas = []

    def salvar_conta(self, conta):
        self.contas.append(conta)
        return True