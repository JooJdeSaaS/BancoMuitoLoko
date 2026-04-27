# Sistema Bancário - Branch 1 (MVC Base)

Este branch contém a implementação inicial do sistema de Caixa Eletrónico utilizando o padrão de arquitetura **MVC (Model-View-Controller)**.

## 🏗️ Estrutura do Projeto

- **Model (`model.py`)**: Define as entidades `Cliente` e `Conta`. Inclui a classe `BancoDados` que simula o armazenamento em memória utilizando listas.
- **View (`view.py`)**: Gere a interface de utilizador (CLI). Responsável por solicitar inputs (Nome, CPF, Saldo) e formatar a exibição dos dados.
- **Controller (`controller.py`)**: Atua como mediador, processando a lógica de criação de objetos e coordenando o fluxo entre a View e o Model.

## 🚀 Como Executar

1. Certifique-se de ter o Python 3.x instalado.
2. No terminal, execute o controlador:
   ```bash
   python3 controller.py
