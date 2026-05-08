class ProcessadorFinanceiro:
    # Constantes para evitar números mágicos
    TAXA_CREDITO = 0.05
    TAXA_DEBITO = 0.02

    def processar_pagamento_credito(self, valor):
        self._executar_processamento(valor, self.TAXA_CREDITO, "crédito")

    def processar_pagamento_debito(self, valor):
        self._executar_processamento(valor, self.TAXA_DEBITO, "débito")

    def _executar_processamento(self, valor, taxa, tipo):
        if valor <= 0:
            print("Valor inválido")
            return

        valor_com_taxa = valor * (1 + taxa)
        print(f"Processando {tipo}: R$ {valor_com_taxa:.2f}")