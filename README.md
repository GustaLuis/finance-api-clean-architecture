# 🏦 Finance API — Clean Architecture

API REST de finanças pessoais construída com **FastAPI**, estruturada seguindo os princípios da **Clean Architecture** (Ports & Adapters), como projeto de estudo de arquitetura de software backend.

## 🎯 Objetivo

Este projeto não é só mais um CRUD — o foco é praticar **separação de responsabilidades** e **inversão de dependência**: as regras de negócio (domínio) não conhecem detalhes de banco de dados, framework web ou qualquer infraestrutura externa.

## 🧱 Arquitetura

```
domain/             → entidades e regras de negócio puras (sem dependências externas)
application/        → casos de uso, orquestram o domínio
infrastructure/      → implementações concretas (FastAPI, SQLAlchemy, JWT, etc.)
```

A regra de ouro: **as dependências sempre apontam para dentro**.

```
infrastructure  →  application  →  domain
   (sabe de tudo)   (sabe do domain)   (não sabe de nada externo)
```

- `domain/` nunca importa nada de `infrastructure/`
- `application/` depende apenas de `domain/` (recebe implementações via injeção de dependência)
- `infrastructure/` implementa as interfaces definidas em `domain/repositories/`

## 📂 Estrutura de pastas

```
finance-api-clean-architecture/
├── domain/
│   ├── entities/              # Account, Transaction — regras de negócio
│   ├── repositories/          # interfaces abstratas (ports)
│   └── exceptions.py          # exceções de domínio
├── application/
│   ├── use_cases/             # ex: CreateTransactionUseCase
│   └── dtos/                  # objetos de entrada/saída dos use cases
├── infrastructure/
│   ├── database/
│   │   ├── models.py          # modelos SQLAlchemy
│   │   ├── session.py
│   │   └── repositories/      # implementações concretas dos repositórios
│   └── web/
│       ├── routers/           # endpoints FastAPI
│       ├── schemas/           # Pydantic (request/response)
│       └── dependencies.py    # injeção de dependência (Depends)
├── tests/
├── main.py
└── requirements.txt
```

## ✅ Implementado até agora

- [x] Entidade `Account` com regras de saque/depósito (`withdraw`, `deposit`)
- [x] Entidade `Transaction`
- [x] Interfaces de repositório (`AccountRepository`, `TransactionRepository`)
- [x] Caso de uso `CreateTransactionUseCase`
- [x] Implementação SQLAlchemy dos repositórios (SQLite + async)
- [x] Endpoint `POST /transactions/`

## 🚧 Próximos passos

- [ ] Cadastro e autenticação de usuário (JWT)
- [ ] CRUD de contas (`Account`)
- [ ] Transferência entre contas
- [ ] Listagem e relatório de transações por categoria
- [ ] Testes unitários dos use cases com repositórios fake (in-memory)
- [ ] Testes de integração dos endpoints (TestClient)

## 🚀 Como rodar

```bash
# Criar e ativar ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt

# Rodar em modo desenvolvimento
fastapi dev main.py
```

A documentação interativa fica disponível em `http://localhost:8000/docs`.

## 🛠️ Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy 2.0](https://www.sqlalchemy.org/) (async)
- [Pydantic v2](https://docs.pydantic.dev/)
- SQLite (banco local de desenvolvimento)
