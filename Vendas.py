class GerenciadorDeVendas:
    def processar_venda(self, itens, cliente, metodo_pagamento):
        total = self._calcular_total(itens)
        total = self._aplicar_descontos(total, cliente, metodo_pagamento)

        self._processar_pagamento(total, metodo_pagamento)
        self._salvar_relatorio(total, cliente)

        print("Venda processada com sucesso.")

    def _calcular_total(self, itens):
        return sum(item['preco'] * item['quantidade'] for item in itens)

    def _aplicar_descontos(self, total, cliente, metodo_pagamento):
        if cliente.get('tipo') == 'VIP' and metodo_pagamento == 'CARTAO':
            return total * 0.90
        return total

    def _processar_pagamento(self, total, metodo_pagamento):
        if metodo_pagamento == 'CARTAO':
            print(f"Cobrando R$ {total:.2f} no cartão de crédito...")
        elif metodo_pagamento == 'BOLETO':
            print(f"Gerando boleto no valor de R$ {total:.2f}...")

    def _salvar_relatorio(self, total, cliente):
        relatorio = (
            f"Relatório de Venda\n"
            f"Cliente: {cliente['name']}\n"
            f"Total: R$ {total:.2f}\n"
            f"{'-' * 20}\n"
        )
        with open("relatorio_vendas.txt", "a") as f:
            f.write(relatorio)