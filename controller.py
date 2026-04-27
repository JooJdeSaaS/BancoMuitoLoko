from model import Cliente, Conta, BancoDados
from view import BancoView

class BancoController:
    def __init__(self):
        self.model_db = BancoDados()
        self.view = BancoView()

    def iniciar_cadastro(self):
        # 1. Recebe dados da View
        nome, cpf, saldo = self.view.exibir_menu_inicial()

        # 2. Instancia as classes do Model
        novo_cliente = Cliente(nome, cpf)
        nova_conta = Conta(novo_cliente, saldo)

        # 3. Salva no "Banco de Dados"
        self.model_db.salvar_conta(nova_conta)

        # 4. Comanda a View para exibir o resultado
        self.view.mostrar_conta_criada(nova_conta)

if __name__ == "__main__":
    app = BancoController()
    app.iniciar_cadastro()