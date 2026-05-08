#Code Smells:
#LPL

class Endereco:
    def __init__(self, rua, numero, bairro, cidade, estado, cep):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.bairro}, {self.cidade}/{self.estado} CEP: {self.cep}"

class Telefone:
    def __init__(self, ddd, numero):
        self.ddd = ddd
        self.numero = numero

    def __str__(self):
        return f"({self.ddd}) {self.numero}"

class Funcionario:
    def __init__(self, nome, cargo, salario, endereco, telefone):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.endereco = endereco  # Objeto da classe Endereco
        self.telefone = telefone  # Objeto da classe Telefone

    def exibir_dados(self):
        print(f"Funcionario: {self.nome} - {self.cargo}")
        print(f"Contato: {self.telefone}")
        print(f"Endereço: {self.endereco}")