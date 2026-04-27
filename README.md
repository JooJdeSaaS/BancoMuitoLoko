# Sistema Bancário - Branch 3: Clean Architecture

Este é o estágio final da refatoração do sistema bancário focado em **escalabilidade**, **testabilidade** e **independência de tecnologia**. O projeto agora segue rigorosamente os princípios da Arquitetura Limpa e o **DIP (Dependency Inversion Principle)**.

## 🚀 O que há de novo?

Nesta branch, o sistema foi totalmente desacoplado em camadas para garantir que as regras de negócio não dependam de detalhes técnicos como o tipo de banco de dados ou a interface do usuário.

### 🛠️ Camadas do Projeto
* **Domínio (`domain.py`)**: Contém as entidades (`Cliente`, `Conta`) e a interface do repositório (`IContaRepository`). É o núcleo que define as regras fundamentais do banco.
* **Casos de Uso (`use_cases.py`)**: Camada de aplicação que orquestra o fluxo de dados (Saque e Depósito), dependendo apenas de abstrações.
* **Infraestrutura (`repository.py`)**: Implementação real da persistência. Os dados agora são salvos em um arquivo **TXT**, permitindo que o saldo e o histórico sobrevivam ao fechamento do programa.
* **Interface (`view.py`)**: Camada de interação (CLI), responsável por coletar entradas do usuário e exibir resultados na tela.
* **Controlador (`controller.py`)**: O orquestrador que recebe as peças prontas (Injeção de Dependência) e gerencia o fluxo de execução.
* **Ponto de Entrada (`main.py`)**: O arquivo principal que "monta" o sistema e inicia o loop de execução.

## 🏗️ Princípios de Engenharia Aplicados
* **DIP (Princípio de Inversão de Dependência)**: O núcleo do banco é independente de tecnologia. Isso permite trocar o armazenamento de TXT para SQL alterando apenas uma linha no arquivo `main.py`.
* **Persistência de Dados**: Implementação de leitura e escrita em arquivo com persistência real de saldo e histórico de operações.
* **SRP (Single Responsibility Principle)**: Cada componente do sistema tem uma única responsabilidade clara, facilitando a manutenção futura no Linux.

## 📋 Como Executar

Certifique-se de estar no ambiente Linux (Ubuntu/Debian) com o Python 3 instalado.

1.  Acesse a pasta do projeto no terminal:
    ```bash
    cd /home/joojdesaas/PycharmProjects/BancoMuitoLoko
    ```
2.  Execute o arquivo principal:
    ```bash
    python3 main.py
    ```

## 📂 Estrutura de Arquivos
```text
.
├── domain.py       # Entidades e Interfaces (Abstração)
├── use_cases.py    # Lógica de Negócio (Regras de Aplicação)
├── repository.py   # Persistência em arquivo TXT (Infraestrutura)
├── view.py         # Telas e Menus de interação (Interface)
├── controller.py   # Orquestrador de Fluxo
├── main.py         # Ponto de entrada do sistema (Bootstrap)
└── banco.txt       # Base de dados em texto (Gerado automaticamente)
