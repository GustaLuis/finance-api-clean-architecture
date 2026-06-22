# Finance API

API REST para controle financeiro pessoal, construída com FastAPI e estruturada seguindo os princípios da Clean Architecture.

Projeto pessoal para estudo de arquitetura de software backend — o domínio (regras de negócio) é mantido isolado de detalhes de implementação como framework web e banco de dados, permitindo testar e evoluir a lógica de negócio sem depender de infraestrutura externa.

## Arquitetura

O código é organizado em três camadas, com a regra de que as dependências sempre apontam para dentro:

```
infrastructure  →  application  →  domain
```

- **domain/** — entidades e regras de negócio puras. Não importa nada de FastAPI, SQLAlchemy ou Pydantic.
- **application/** — casos de uso que orquestram as entidades de domínio. Depende apenas de `domain/`, recebendo implementações concretas via injeção de dependência.
- **infrastructure/** — implementações concretas: endpoints FastAPI, modelos SQLAlchemy, schemas Pydantic.

`domain/` define interfaces abstratas de repositório (`AccountRepository`, `TransactionRepository`); `infrastructure/` as implementa usando SQLAlchemy. Isso mantém os casos de uso testáveis sem necessidade de um banco de dados real — em testes, as interfaces podem ser substituídas por implementações in-memory.

```
domain/
├── entities/          # Account, Transaction — dados e regras de negócio
├── repositories/       # interfaces abstratas (ports)
└── exceptions.py

application/
├── use_cases/          # ex: CreateTransactionUseCase
└── dtos/                # objetos de entrada/saída dos use cases

infrastructure/
├── database/
│   ├── models.py        # modelos SQLAlchemy
│   └── repositories/    # implementações concretas dos repositórios
└── web/
    ├── routers/          # endpoints FastAPI
    ├── schemas/          # validação Pydantic
    └── dependencies.py   # injeção de dependência
```

## Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy 2.0](https://www.sqlalchemy.org/) (async)
- [Pydantic v2](https://docs.pydantic.dev/)
- SQLite (desenvolvimento local)

## Como rodar

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -r requirements.txt

fastapi dev main.py
```

Documentação interativa disponível em `http://localhost:8000/docs`.

## Status atual

O domínio modela contas (`Account`) e transações (`Transaction`), com a regra de saldo (saque/depósito) encapsulada na própria entidade. O endpoint `POST /transactions/` está funcional, criando uma transação e atualizando o saldo da conta correspondente.

Em desenvolvimento: CRUD completo de contas, autenticação via JWT, transferência entre contas, relatórios por categoria e cobertura de testes.