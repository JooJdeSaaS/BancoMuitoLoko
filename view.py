import os

class BancoView:
    def exibir_menu(self):
        print("\n" + "="*30)
        print("   CAIXA ELETRÔNICO  ")
        print("="*30)
        print("1. Abrir Conta")
        print("2. Depósito")
        print("3. Saque")
        print("4. Extrato")
        print("5. Render Poupança") # Nova opção
        print("6. Sair")
        return input("\nEscolha uma opção: ")

    def tela_cadastro(self):
        nome = input("Nome do Titular: ")
        cpf = input("CPF (apenas números): ")
        saldo = float(input("Saldo Inicial: R$ "))
        return nome, cpf, saldo

    def tela_operacao(self, tipo):
        cpf = input(f"Confirme o CPF para {tipo}: ")
        valor = float(input(f"Valor do {tipo}: R$ "))
        return cpf, valor

    def tela_extrato(self):
        return input("Digite o CPF para ver o extrato: ")

    def mostrar_extrato(self, conta):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n--- EXTRATO: {conta.cliente.nome} ---")
        for h in conta.historico:
            print(h)
        print(f"\nSALDO ATUAL: R$ {conta.saldo:.2f}")
        print("-" * 30)

    def mostrar_mensagem(self, msg):
        print(f"\n>>> {msg}")