class Pais:
    def __init__(self, nome):
        self.nome = nome


class Estado:
    def __init__(self, nome, pais):
        self.nome = nome
        self.pais = pais

    def obter_nome_pais(self):
        return self.pais.nome


class Endereco:
    def __init__(self, rua, estado):
        self.rua = rua
        self.estado = estado

    def obter_nome_pais(self):
        return self.estado.obter_nome_pais()


class Cliente:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def obter_pais_cliente(self):
        return self.endereco.obter_nome_pais()


class Pedido:
    def __init__(self, cliente, valor):
        self.cliente = cliente
        self.valor = valor

    def obter_pais_destino(self):
        # O Pedido agora fala apenas com o seu 'amigo' Cliente
        return self.cliente.obter_pais_cliente()


# Sem acesso profundo
def verificar_frete_internacional(pedido):
    pais_destino = pedido.obter_pais_destino()

    if pais_destino != "Brasil":
        print("Sujeito a taxa de importação.")
    else:
        print("Frete nacional padrão.")