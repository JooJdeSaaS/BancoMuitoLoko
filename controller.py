from model import Cliente, Conta, BancoDados
from service import BancoService
from view import BancoView


class BancoController:
    def __init__(self):
        self.db = BancoDados()
        self.service = BancoService(self.db)
        self.view = BancoView()

    def rodar(self):
        while True:
            opcao = self.view.exibir_menu_principal()

            if opcao == "1":
                nome, cpf, saldo = self.view.solicitar_dados_cadastro()
                nova_conta = Conta(Cliente(nome, cpf), saldo)
                self.db.salvar_conta(nova_conta)
                self.view.mostrar_mensagem("Conta criada!")

            elif opcao == "2":
                cpf, valor = self.view.solicitar_valor("Depósito")
                sucesso, msg = self.service.depositar(cpf, valor)
                self.view.mostrar_mensagem(msg)

            elif opcao == "3":
                cpf, valor = self.view.solicitar_valor("Saque")
                sucesso, msg = self.service.sacar(cpf, valor)
                self.view.mostrar_mensagem(msg)

            elif opcao == "4":
                cpf = input("Digite o CPF para extrato: ")
                hist = self.service.obter_extrato(cpf)
                if hist:
                    self.view.mostrar_extrato(hist)
                else:
                    self.view.mostrar_mensagem("Conta não encontrada.")

            elif opcao == "5":
                break


if __name__ == "__main__":
    BancoController().rodar()