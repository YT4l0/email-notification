
# API de Notificação por E-mail com Django Rest Framework

Este projeto implementa uma API RESTful para o envio de notificações por e-mail. A aplicação é construída com Django e Django Rest Framework, permitindo que um cliente envie os dados de uma notificação (destinatário, assunto e mensagem) para um endpoint, que então processa e dispara o e-mail usando um serviço SMTP.

## Como Funciona

O fluxo de uma notificação segue os seguintes passos:

1.  Um cliente faz uma requisição `POST` para o endpoint `/api/notify/` com os dados da notificação em formato JSON.
2.  O `urls.py` principal do projeto direciona a requisição para o `urls.py` do app `api`.
3.  A rota em `api/urls.py` aciona a `NotificationView`.
4.  A `NotificationView` utiliza o `NotificationSerializer` para validar os dados recebidos (`email`, `subject`, `message`).
5.  Se os dados forem válidos, a view utiliza a função `send_mail` nativa do Django para enviar o e-mail, usando as credenciais configuradas no `settings.py`.
6.  Após o envio bem-sucedido, um registro da notificação é salvo no banco de dados, utilizando o modelo `Notification`.
7.  A API retorna uma resposta JSON confirmando o sucesso ou informando o erro.

## Estrutura do Projeto

A organização das pastas e arquivos segue as melhores práticas do Django:

```
email-notification/
├── venv/                      # Ambiente virtual Python com as dependências
├── api/                       # App Django responsável por toda a lógica da API
│   ├── migrations/            # Arquivos de migração do banco de dados
│   ├── admin.py               # Configuração do modelo no painel de admin
│   ├── apps.py                # Configuração do app 'api'
│   ├── models.py              # Modelo de dados 'Notification'
│   ├── serializers.py         # Serializador que valida os dados de entrada
│   ├── tests.py               # Arquivo para testes unitários
│   ├── urls.py                # Rotas específicas da API (ex: /notify/)
│   └── views.py               # O cérebro da aplicação, onde o e-mail é enviado
├── notificacoes_project/      # Pasta de configurações do projeto Django
│   ├── settings.py            # Configurações globais (apps, banco de dados, e-mail)
│   ├── urls.py                # Rotas principais do projeto
│   └── wsgi.py
├── db.sqlite3                 # Banco de dados SQLite
├── manage.py                  # Script principal para gerenciar o projeto
├── requirements.txt           # Lista de dependências Python para o projeto
└── Readme.md                  # Este arquivo
```

## Guia de Instalação e Execução (Linux/WSL)

Siga este guia passo a passo para configurar e executar o projeto em um ambiente Linux ou WSL (Subsistema do Windows para Linux).

#### 1\. Pré-requisitos

Primeiro, garanta que o Python 3 e o pacote `venv` (para ambientes virtuais) estão instalados no seu sistema.

```sh
sudo apt update
sudo apt install python3 python3-venv
```

#### 2\. Configuração do Ambiente Virtual

É fundamental isolar as dependências do projeto.

```sh
# 1. Na pasta raiz 'email-notification', crie o ambiente virtual:
python3 -m venv venv

# 2. Ative o ambiente (faça isso TODA VEZ que for trabalhar no projeto):
source venv/bin/activate
```

Após a ativação, o nome do seu terminal mudará para indicar que você está dentro do ambiente, exibindo `(venv)`.

#### 3\. Instalação das Dependências

Com o ambiente `(venv)` ativo, instale todas as bibliotecas necessárias com um único comando:

```sh
pip install -r requirements.txt
```

#### 4\. Configuração do Serviço de E-mail

Para que o envio de e-mails funcione, você precisa configurar suas credenciais.

1.  Abra o arquivo `notificacoes_project/settings.py`.

2.  Vá até o final do arquivo e adicione ou edite as seguintes variáveis:

    ```python
    # settings.py

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'  # Servidor SMTP do Gmail
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = 'seu-email-aqui@gmail.com'  # O e-mail que vai ENVIAR a notificação
    EMAIL_HOST_PASSWORD = 'sua_senha_de_app_de_16_letras' # A senha de app gerada no Google
    ```

> **Importante:** O `EMAIL_HOST_PASSWORD` **não é** a sua senha comum do Google. É uma **"Senha de App"** de 16 letras, que você deve gerar na seção de segurança da sua Conta Google após ativar a "Verificação em duas etapas".

#### 5\. Preparação do Banco de Dados

Crie as tabelas necessárias no banco de dados `db.sqlite3`.

```sh
python3 manage.py makemigrations
python3 manage.py migrate
```

#### 6\. Execução do Servidor

Com tudo configurado, inicie o servidor de desenvolvimento:

```sh
python3 manage.py runserver
```

A API estará disponível em `http://127.0.0.1:8000/`. Deixe este terminal rodando.

-----

## Como Testar a API

Com o servidor em execução, **abra um novo terminal** e use o comando `curl` para fazer uma requisição `POST` para o endpoint de notificação.

```sh
curl -X POST http://127.0.0.1:8000/api/notify/ \
-H "Content-Type: application/json" \
-d '{"email": "email.destinatario@example.com", "subject": "Assunto do Teste", "message": "Esta é uma mensagem de teste da API."}'
```

**Não se esqueça** de substituir `email.destinatario@example.com` pelo endereço de e-mail para o qual você quer enviar o teste.

### Resposta Esperada

Se a requisição for bem-sucedida, você receberá a seguinte resposta JSON, e o e-mail será entregue na caixa de entrada do destinatário:

```json
{"message":"Notificação enviada com sucesso!"}
```