import os

class BancoView:
    def exibir_menu_principal(self):
        print("\n--- CAIXA ELETRÔNICO ---")
        print("1. Criar Conta")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Ver Extrato")
        print("5. Sair")
        return input("Escolha uma opção: ")

    def solicitar_dados_cadastro(self):
        nome = input("Nome: ")
        cpf = input("CPF: ")
        saldo = float(input("Saldo Inicial: "))
        return nome, cpf, saldo

    def solicitar_valor(self, operacao):
        cpf = input("Confirme seu CPF: ")
        valor = float(input(f"Valor do {operacao}: R$ "))
        return cpf, valor

    def mostrar_mensagem(self, msg):
        print(f"\n>>> {msg}")

    def mostrar_extrato(self, historico):
        print("\n" + " EXTRATO BANCÁRIO ".center(30, "="))
        for item in historico:
            print(item)
        print("="*30)