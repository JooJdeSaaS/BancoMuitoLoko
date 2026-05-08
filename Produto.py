class Produto:
    """Classe de Domínio: Contém apenas os dados e lógica intrínseca."""
    def __init__(self, id_produto, nome, preco):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco

    def calcular_preco_com_imposto(self):
        return self.preco * 1.15

class ProdutoRepository:
    """Responsável pela persistência (Banco de Dados)."""
    def salvar(self, produto: Produto):
        # Lógica de banco de dados isolada
        sql = (f"INSERT INTO produtos (id, nome, preco) "
               f"VALUES ({produto.id_produto}, '{produto.nome}', {produto.preco});")
        print(sql)

class ProdutoExporter:
    """Responsável pela exportação de formatos."""
    def para_xml(self, produto: Produto):
        return (f"<produto>"
                f"<id>{produto.id_produto}</id>"
                f"<nome>{produto.nome}</nome>"
                f"<preco>{produto.preco}</preco>"
                f"</produto>")