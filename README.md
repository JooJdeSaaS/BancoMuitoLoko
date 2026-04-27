# Sistema Bancário - Branch 2: Multicamadas & Operações

Esta versão do projeto implementa a lógica financeira de depósitos e saques, utilizando uma **Arquitetura Multicamadas** para separar as regras de negócio da interface.

## 📁 Organização de Pastas e Camadas

A estrutura foi desenhada para garantir que cada arquivo tenha uma responsabilidade única:

- **`model.py` (Dados)**: Define as entidades `Cliente`, `Conta` e simula a persistência no `BancoDados`.
- **`service.py` (Negócios)**: Contém as regras bancárias (ex: validação de saldo para saque).
- **`view.py` (Interface)**: Gere as entradas e saídas de texto no terminal.
- **`controller.py` (Controle)**: Orquestra o fluxo de execução entre todas as camadas.



## 🛠️ Funcionalidades Adicionadas
- **Depósitos e Saques**: Agora é possível movimentar o saldo da conta.
- **Histórico/Extrato**: Todas as operações são registradas e podem ser visualizadas.
- **Validação de Negócio**: O sistema impede saques superiores ao saldo disponível.

## 🚀 Como Executar
Sempre inicie o programa pelo controlador:
```bash
python3 controller.py
