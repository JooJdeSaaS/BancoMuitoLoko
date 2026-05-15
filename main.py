from repository import ArquivoContaRepository
from use_cases import RealizarOperacaoUseCase
from view import BancoView
from controller import BancoController


def bootstrap():
    repositorio = ArquivoContaRepository(arquivo="banco.txt")

    casos_de_uso = RealizarOperacaoUseCase(repositorio)

    interface = BancoView()

    app = BancoController(repositorio, casos_de_uso, interface)

    app.rodar()


if __name__ == "__main__":
    bootstrap()