import sys


class BancoController:
    def __init__(self, repo, uc, view):
        self.repo = repo
        self.uc = uc
        self.view = view

        self.comandos = {
            "1": self._executar_cadastro,
            "2": self._executar_deposito,
            "3": self._executar_saque,
            "4": self._executar_extrato,
            "5": self._executar_investimento,  # Nova opção
            "6": self._executar_sair
        }

    def _executar_cadastro(self):
        nome, cpf, saldo = self.view.tela_cadastro()

        from domain import Cliente, Conta
        nova_conta = Conta(Cliente(nome, cpf), saldo)

        self.repo.salvar(nova_conta)
        self.view.mostrar_mensagem("Conta criada e salva com sucesso!")

    def _executar_deposito(self):
        cpf, valor = self.view.tela_operacao("Depósito")
        sucesso, msg = self.uc.depositar(cpf, valor)
        self.view.mostrar_mensagem(msg)

    def _executar_saque(self):
        cpf, valor = self.view.tela_operacao("Saque")
        sucesso, msg = self.uc.sacar(cpf, valor)
        self.view.mostrar_mensagem(msg)

    def _executar_extrato(self):
        cpf = self.view.tela_extrato()
        conta = self.repo.buscar_por_cpf(cpf)
        if conta:
            self.view.mostrar_extrato(conta)
        else:
            self.view.mostrar_mensagem("Erro: Conta não encontrada.")

    def _executar_investimento(self):
        cpf = self.view.tela_extrato()  # Reutiliza a tela de CPF
        sucesso, msg = self.uc.investir_poupanca(cpf)
        self.view.mostrar_mensagem(msg)

    def _executar_sair(self):
        self.view.mostrar_mensagem("Encerrando o sistema... Até logo!")
        sys.exit()

    def rodar(self):
        while True:
            opcao = self.view.exibir_menu()

            acao = self.comandos.get(opcao, lambda: self.view.mostrar_mensagem("Opção Inválida!"))
            acao()