class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Conta:
    def __init__(self, cliente, saldo_inicial):
        self.cliente = cliente
        self.saldo = saldo_inicial
        self.numero_conta = "001-" + str(cliente.cpf[-3:])
        self.historico = [f"Abertura de conta: R$ {saldo_inicial:.2f}"]

    def adicionar_ao_historico(self, mensagem):
        self.historico.append(mensagem)

class BancoDados:
    def __init__(self):
        self.contas = []

    def salvar_conta(self, conta):
        self.contas.append(conta)

    def buscar_conta_por_cpf(self, cpf):
        for conta in self.contas:
            if conta.cliente.cpf == cpf:
                return conta
        return None