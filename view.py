import os

class BancoView:
    def exibir_menu_inicial(self):
        print("\n" + "=" * 30)
        print("      CAIXA ELETRÔNICO      ")
        print("=" * 30)
        print("CADASTRO DE NOVA CONTA")

        nome = input("Nome do Titular: ")
        cpf = input("CPF: ")
        try:
            saldo = float(input("Saldo Inicial: R$ "))
        except ValueError:
            print("Valor inválido! Definindo saldo como R$ 0.00")
            saldo = 0.0

        return nome, cpf, saldo

    def mostrar_conta_criada(self, conta):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + "Check-out de Cadastro".center(30, "-"))
        print(f"Titular: {conta.cliente.nome}")
        print(f"CPF:     {conta.cliente.cpf}")
        print(f"Conta:   {conta.numero_conta}")
        print(f"Saldo:   R$ {conta.saldo:.2f}")
        print("-" * 30)
        print("Conta cadastrada com sucesso!")