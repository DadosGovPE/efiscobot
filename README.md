# E-Fisco Bot

#### Bot que executa diversas tarefas no sistema E-Fisco do Governo PE.

## Webdrivers aceitos

Firefox: geckodriver.exe (incluso arquivo .rar no projeto)

## Como rodar

#### 1. Certifique-se do geckdrive.exe

Não esqueça que este arquivo deve está no _path_ das variáveis de ambientes da máquina.

#### 2. Crie um arquivo .env

O template está na raiz do projeto `.env_template`. Renomeie para `.env`.

#### 3. No cmd do MS Windows:

```
git clone...
cd efiscobot
python -m venv .ve
.ve\Scripts\activate
pip install -r requirements.txt
ipython -i src\init.py
```

Dessa forma o código rodará de forma iterativa no ipython para o dev poder prototipar alternativas.

## Tarefas
- [ ] Alternativas ao captcha na hora do login.