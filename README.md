# Seleção FESF-SUS - 2 F.C

![Docker](https://img.shields.io/badge/Docker-enabled-blue)
![Docker Compose](https://img.shields.io/badge/Docker--Compose-ready-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green)
![Next.js](https://img.shields.io/badge/Next.js-15-black)

Projeto desenvolvido para o processo seletivo da FESF-SUS.

Este repositório contempla a conteinerização funcional da aplicação utilizando Docker e Docker Compose, permitindo a inicialização completa e integrada do ambiente.

---

# Tecnologias Utilizadas

- Docker
- Docker Compose
- FastAPI
- PostgreSQL
- Next.js
- React
- TypeScript

---

# Estrutura do Projeto

```txt
backend/
frontend/
docker-compose.yml
```

---

# Containerização

A aplicação foi conteinerizada utilizando:

## Backend
- Python 3.13
- FastAPI

## Frontend
- Node.js 22
- Next.js

## Banco de Dados
- PostgreSQL 17

---

# Arquivos Docker

## Backend
- Dockerfile

## Frontend
- Dockerfile

## Orquestração
- docker-compose.yml

---

# Como executar

```bash
docker compose up --build
```

---

# Serviços Disponíveis

## Frontend

```txt
http://localhost:3000
```

---

## Backend

```txt
http://localhost:8000
```

---

## Swagger

```txt
http://localhost:8000/docs
```

---

# Funcionalidades

- Inicialização automatizada dos serviços
- Comunicação entre containers
- Persistência de banco PostgreSQL
- API REST funcional
- Frontend integrado ao backend
- Ambiente full stack integrado

---


## Preview

### Dashboard Desktop

![Dashboard Desktop](./docs/DASHBOARD-DESKTOP.png)

### Dashboard Mobile

![Dashboard Mobile](./docs/DASHBOARD-MOBILE1.png)
![Dashboard Mobile](./docs/DASHBOARD-MOBILE2.png)
![Dashboard Mobile](./docs/DASHBOARD-MOBILE3.png)

### Documentação da API

![Swagger API](./docs/SWAGGER-API.png)
```
# Estrutura do Projeto

```txt
backend/
frontend/
docker-compose.yml
README.md
```

---

# Como executar localmente

## Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# Executando com Docker

```bash
docker compose up --build
```

---

# Endpoints principais

## Patients
- GET /patients
- POST /patients
- DELETE /patients/{id}

## Appointments
- GET /appointments
- POST /appointments
- PUT /appointments/{id}

## Dashboard
- GET /dashboard

---

# Documentação Swagger

```txt
http://localhost:8000/docs
```

---

# Autor

Mateus Sagrilo Brasileiro Lima

- GitHub:
https://github.com/MateusSagrilo

- LinkedIn:
https://www.linkedin.com/in/mateus-sagrilo-brasileiro-lima/