
# 🌡 Sistema de Monitoramento de Equipamentos IoT

Este projeto é uma aplicação desenvolvida para monitorar equipamentos IoT, rastreando dados como **localização**, **temperatura**, **nome** e **status operacional** de cada dispositivo.

## Funcionalidades

- Exibir a lista de equipamentos monitorados.
- Visualizar os detalhes de cada equipamento individualmente.
- Monitorar temperatura e localização em tempo real.
- Alterar o status operacional dos equipamentos (Operacional/Não Operacional).
  
## Tecnologias Utilizadas

- **Backend**: Django + Django REST Framework
- **Frontend**: (React ou outra tecnologia, se houver)
- **Banco de Dados**: (SQLite, PostgreSQL, etc.)
- **API**: RESTful API para comunicação com dispositivos IoT

## Como Executar o Projeto

### Pré-requisitos

- **Python 3.9+**
- **Django 4.x**
- **Node.js (se houver front-end com React)**

### Passo a Passo

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/adryanhy/iotUbs.git
   cd iotUbs
   ```

2. **Crie e ative um ambiente virtual:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # No Windows use: venv\Scripts\activate
   ```

3. **Instale as dependências do projeto:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Realize as migrações do banco de dados:**

   ```bash
   python manage.py migrate
   ```

5. **Execute a aplicação:**

   ```bash
   python manage.py runserver
   ```

6. **Acesse no navegador:**

   ```
   http://localhost:8000
   ```

### Para rodar o front-end:

Se estiver utilizando React ou outra biblioteca:

```bash
cd frontend
npm install
npm start
```

## Endpoints Principais

- `GET /equipamentos/` – Lista todos os equipamentos.
- `GET /equipamentos/<id>` – Exibe detalhes de um equipamento específico.
- `POST /equipamentos/` – Adiciona um novo equipamento.
- `PUT /equipamentos/<id>` – Atualiza um equipamento.
- `DELETE /equipamentos/<id>` – Remove um equipamento.

## Estrutura do Projeto

```bash
.
├── iotUbs/                  # Diretório principal do projeto Django
│   ├── settings.py          # Configurações do Django
│   ├── urls.py              # Rotas do Django
│   └── ...
├── equipamentos/            # App responsável pelo gerenciamento de equipamentos
│   ├── models.py            # Modelos de dados (Equipamentos)
│   ├── serializers.py       # Serializadores para API
│   ├── views.py             # Lógica das views (API REST)
│   └── ...
├── frontend/                # Diretório do front-end (React ou outra tecnologia)
│   └── ...
├── db.sqlite3               # Banco de dados SQLite (pode variar)
└── requirements.txt         # Dependências do projeto
```

