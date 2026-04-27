class BancoService:
    def __init__(self, db):
        self.db = db

    def depositar(self, cpf, valor):
        conta = self.db.buscar_conta_por_cpf(cpf)
        if conta and valor > 0:
            conta.saldo += valor
            conta.adicionar_ao_historico(f"Depósito: + R$ {valor:.2f}")
            return True, "Depósito realizado com sucesso!"
        return False, "Erro ao realizar depósito."

    def sacar(self, cpf, valor):
        conta = self.db.buscar_conta_por_cpf(cpf)
        if not conta:
            return False, "Conta não encontrada."

        if 0 < valor <= conta.saldo:
            conta.saldo -= valor
            conta.adicionar_ao_historico(f"Saque: - R$ {valor:.2f}")
            return True, "Saque realizado!"
        return False, "Saldo insuficiente ou valor inválido."

    def obter_extrato(self, cpf):
        conta = self.db.buscar_conta_por_cpf(cpf)
        return conta.historico if conta else None