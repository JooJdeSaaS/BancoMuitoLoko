import os
from domain import IContaRepository, Conta, Cliente


class ArquivoContaRepository(IContaRepository):
    def __init__(self, arquivo="banco.txt"):
        self.arquivo = arquivo

    def salvar(self, conta):
        contas = self._ler_todas()
        contas[conta.cliente.cpf] = conta
        self._escrever_todas(contas)

    def buscar_por_cpf(self, cpf):
        contas = self._ler_todas()
        return contas.get(cpf)

    def _ler_todas(self):
        contas = {}
        if not os.path.exists(self.arquivo):
            return contas

        with open(self.arquivo, "r") as f:
            for linha in f:
                if not linha.strip(): continue
                partes = linha.strip().split(";")
                if len(partes) < 4: continue

                nome, cpf, saldo, hist_str = partes
                cliente = Cliente(nome, cpf)
                # Reconstrói a conta com o histórico salvo
                contas[cpf] = Conta(cliente, float(saldo), hist_str.split("|"))
        return contas

    def _escrever_todas(self, contas):
        with open(self.arquivo, "w") as f:
            for c in contas.values():
                hist_str = "|".join(c.historico)
                f.write(f"{c.cliente.nome};{c.cliente.cpf};{c.saldo};{hist_str}\n")