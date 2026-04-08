# FinFlow API Portal (White Label) — Centralizador de Documentação

Portal genérico (white label) para centralizar a documentação OpenAPI de múltiplos microsserviços. Sem expor endpoints ou domínios reais.

## Problema
> A empresa possuía diversos microsserviços descentralizados, forçando os desenvolvedores a buscarem a documentação (Swagger) de cada um em URLs diferentes.

## Solução
> Desenvolvimento de um portal centralizado com FastAPI que consome de forma assíncrona os schemas OpenAPI de todos os serviços e os renderiza em uma única interface usando Jinja2.

## Impacto
> Aumento da produtividade e melhoria na Developer Experience (DX).

## Tecnologias
- Python 3
- FastAPI
- Jinja2
- aiohttp
- Pydantic

## Arquitetura e Organização
```
/app
  /routers
    api_docs.py
  /services
    fetch_openapi.py
  /templates
    index.html
  /static
    /css
      style.css
  main.py
requirements.txt
```

- `app/services/fetch_openapi.py`: simula chamadas assíncronas para obter schemas OpenAPI (mock) de 4 microsserviços: Auth, Payments, KYC, Loans.
- `app/routers/api_docs.py`: rota principal (`/`) que agrega os schemas e renderiza a página.
- `app/templates/index.html`: template Jinja2 que exibe cards com metadados e endpoints.
- `app/static/css/style.css`: estilo moderno, inspirado em Swagger/Redoc.
- `app/main.py`: inicialização do FastAPI, configuração de estáticos e templates. Swagger (`/docs`), Redoc (`/redoc`) e OpenAPI JSON (`/openapi.json`) habilitados.
- `app/routers/mock_apis.py`: endpoints fictícios (Auth, Payments, KYC, Loans) para popular a documentação Swagger.

## Como executar
1. Crie um ambiente virtual (opcional, porém recomendado):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```
2. Instale dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Rode o servidor:
   ```bash
   uvicorn app.main:app --reload
   ```
4. Acesse:
   - Portal: `http://localhost:8000/`
   - Swagger UI: `http://localhost:8000/docs`
   - Redoc: `http://localhost:8000/redoc`
   - OpenAPI JSON: `http://localhost:8000/openapi.json`

Observação: este é um projeto demonstrativo. Nenhuma API real é consultada; o serviço retorna dicionários com estrutura "OpenAPI-like". Os endpoints em `/mock/...` devolvem dados fictícios para fins de documentação e testes locais.

## Decisões de Engenharia
- Mock assíncrono: uso de `asyncio.gather` para representar paralelismo de chamadas a serviços.
- Pydantic para tipagem/validação do schema interno antes de gerar dicionários.
- UI minimalista, porém escalável: fácil integrar links reais de Swagger/Redoc futuramente.


<img width="1891" height="865" alt="image" src="https://github.com/user-attachments/assets/6ab4a53b-794e-4503-9d71-56a6c789d961" />

<img width="1893" height="775" alt="image" src="https://github.com/user-attachments/assets/76ba44c5-bc55-4762-80bb-14f3442b10f3" />

<img width="1883" height="860" alt="image" src="https://github.com/user-attachments/assets/8c67e516-528f-4be9-ab41-c4306bdf2bec" />




---
Feito com FastAPI e carinho para melhorar a DX.
