# Email Notification API

Este projeto é uma API Django para envio de notificações por e-mail.

## Estrutura de Pastas

```
email-notification/
├── api/                      # App Django responsável pela API de notificações
│   ├── migrations/           # Migrações do banco de dados
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py             # Modelo Notification
│   ├── serializers.py        # Serializador para validação dos dados
│   ├── tests.py
│   ├── urls.py               # Rotas da API
│   └── views.py              # Lógica do envio de e-mail e registro
├── notificacoes_project/     # Projeto principal Django
│   ├── __init__.py
│   ├── settings.py           # Configuração do projeto e do e-mail
│   ├── urls.py               # Rotas principais do projeto
│   └── wsgi.py
├── db.sqlite3                # Banco de dados SQLite
├── manage.py                 # Utilitário de gerenciamento Django
├── requirements.txt          # Dependências do projeto
└── Readme.md                 # Documentação do projeto
```

## Como rodar

1. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

2. Execute as migrações:
   ```sh
   python manage.py migrate
   ```

3. Inicie o servidor:
   ```sh
   python manage.py runserver
   ```

## Enviando uma notificação

Para enviar uma notificação por e-mail, utilize o seguinte comando `curl`:

```sh
curl -X POST http://127.0.0.1:8000/api/notify/ \
-H "Content-Type: application/json" \
-d '{"email": "o email que vai receber", "subject": "Testando 123", "message": "Teste realizado com sucesso"}'
```

- `email`: E-mail do destinatário
- `subject`: Assunto do e-mail
- `message`: Mensagem do e-mail

## Configuração de E-mail

No arquivo [`settings.py`](notificacoes_project/notificacoes_project/settings.py), altere as seguintes variáveis para configurar o envio real de e-mails:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'seuemail.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'qualquer email válido'  # O e-mail que vai ENVIAR
EMAIL_HOST_PASSWORD = 'sua senha de app gerada pela verificação de duas etapas' # A senha de 16 letras do Google
```

> **Atenção:** O `EMAIL_HOST_USER` deve ser um e-mail válido do Gmail e o `EMAIL_HOST_PASSWORD` deve ser a senha de app gerada pelo Google (16 caracteres), após ativar a verificação em duas etapas.

## Endpoints

- `POST /api/notify/`: Envia uma notificação por e-mail.

## Licença
