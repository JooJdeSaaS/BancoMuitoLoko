from datetime import datetime

class Hospede:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

class Quarto:
    def __init__(self, numero, tipo, valor_diaria):
        self.numero = numero
        self.tipo = tipo
        self.valor_diaria = valor_diaria

class Reserva:
    def __init__(self, hospede, quarto, checkin, checkout, cafe_da_manha=False):
        self.hospede = hospede
        self.quarto = quarto
        self.checkin = datetime.strptime(checkin, "%d/%m/%Y")
        self.checkout = datetime.strptime(checkout, "%d/%m/%Y")
        self.cafe_da_manha = cafe_da_manha

    def calcular_total(self):
        dias = (self.checkout - self.checkin).days
        total = dias * self.quarto.valor_diaria
        if self.cafe_da_manha:
            total += 50 * dias
        return total

    def exibir_resumo(self):
        total = self.calcular_total()
        print(f"Reserva criada para {self.hospede.nome} (CPF: {self.hospede.cpf})")
        print(f"Quarto {self.quarto.numero} ({self.quarto.tipo})")
        print(f"De {self.checkin.strftime('%d/%m/%Y')} até {self.checkout.strftime('%d/%m/%Y')}")
        print(f"Total a pagar: R$ {total:.2f}")

# Exemplo de uso
hospede_1 = Hospede("João de Sá", "123.456.789-00", "joao@email.com")
quarto_1 = Quarto(101, "Luxo", 250.0)
reserva_1 = Reserva(hospede_1, quarto_1, "10/05/2026", "15/05/2026", cafe_da_manha=True)

reserva_1.exibir_resumo()