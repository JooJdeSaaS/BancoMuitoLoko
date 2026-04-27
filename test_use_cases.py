import unittest
from unittest.mock import MagicMock
from domain import Conta, Cliente
from use_cases import RealizarOperacaoUseCase


class TestOperacoesBancarias(unittest.TestCase):

    def setUp(self):
        """
        Prepara o ambiente para cada teste.
        O repositório mockado e o caso de uso são comuns a ambos os cenários.
        """
        self.repositorio_mock = MagicMock()
        self.use_case = RealizarOperacaoUseCase(self.repositorio_mock)

    def test_deve_aplicar_rendimento_com_sucesso(self):
        # --- ARRANGE (Organizar) ---
        # 1. Dados iniciais (O cliente aqui age como um Dummy para a Conta)
        cliente = Cliente("João de Sá", "12345678900")
        saldo_inicial = 1000.0
        conta_teste = Conta(cliente, saldo_inicial)
        taxa_teste = 0.01  # 1%

        # 2. STUB: Configuramos o comportamento fixo para retornar a conta teste
        self.repositorio_mock.buscar_por_cpf.return_value = conta_teste

        # --- ACT (Agir) ---
        sucesso, mensagem = self.use_case.investir_poupanca("12345678900", taxa=taxa_teste)

        # --- ASSERT (Aferir) ---
        self.assertTrue(sucesso)
        self.assertEqual(conta_teste.saldo, 1010.0)
        self.assertIn("Rendimento Poupança: + R$ 10.00", conta_teste.historico)

        # MOCK: Verifica se o método salvar foi invocado corretamente
        self.repositorio_mock.salvar.assert_called_once_with(conta_teste)
        self.assertEqual(mensagem, "Rendimento de R$ 10.00 aplicado!")

    def test_deve_realizar_saque_com_sucesso(self):
        # --- ARRANGE (Organizar) ---
        # 1. DUMMY: O cliente é necessário para criar a conta, mas seus dados são irrelevantes aqui.
        dummy_cliente = Cliente("Nome Irrelevante", "00000000000")

        conta_teste = Conta(dummy_cliente, 100.0)
        cpf_teste = "00000000000"
        valor_saque = 30.0

        # 2. STUB: Define o comportamento do mock para este cenário específico
        self.repositorio_mock.buscar_por_cpf.return_value = conta_teste

        # --- ACT (Agir) ---
        sucesso, mensagem = self.use_case.sacar(cpf_teste, valor_saque)

        # --- ASSERT (Aferir) ---
        self.assertTrue(sucesso)
        self.assertEqual(conta_teste.saldo, 70.0)

        # MOCK: Garante que a alteração foi persistida no repositório
        self.repositorio_mock.salvar.assert_called_once_with(conta_teste)
        self.assertIn("Saque: - R$ 30.00", conta_teste.historico)


if __name__ == "__main__":
    unittest.main()