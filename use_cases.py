class RealizarOperacaoUseCase:
    def __init__(self, repository):
        self.repository = repository

    def sacar(self, cpf, valor):
        conta = self.repository.buscar_por_cpf(cpf)
        if conta and 0 < valor <= conta.saldo:
            conta.saldo -= valor
            conta.historico.append(f"Saque: - R$ {valor:.2f}")
            self.repository.salvar(conta)
            return True, "Saque realizado com sucesso!"
        return False, "Saldo insuficiente ou conta não encontrada."

    def depositar(self, cpf, valor):
        conta = self.repository.buscar_por_cpf(cpf)
        if conta and valor > 0:
            conta.saldo += valor
            conta.historico.append(f"Depósito: + R$ {valor:.2f}")
            self.repository.salvar(conta)
            return True, "Depósito realizado com sucesso!"
        return False, "Erro ao processar depósito."