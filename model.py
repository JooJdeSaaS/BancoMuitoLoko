class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Conta:
    def __init__(self, cliente, saldo_inicial):
        self.cliente = cliente
        self.saldo = saldo_inicial
        # O erro estava aqui: precisamos acessar o atributo cpf do objeto cliente
        self.numero_conta = "001-" + str(cliente.cpf[-3:])

class BancoDados:
    def __init__(self):
        self.contas = []

    def salvar_conta(self, conta):
        self.contas.append(conta)
        return True