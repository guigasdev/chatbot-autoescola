# Documentação - Chatbot de Envio de Mensagens no WhatsApp com Integração Twilio

## Descrição Geral
Este projeto implementa um chatbot de envio de mensagens no WhatsApp, integrado com a API Twilio, usando Python e Flask. O bot responde a mensagens enviadas por usuários e é capaz de realizar diferentes interações automatizadas, relacionadas a AutoEscola Ari. Além disso, o bot faz uso da API OpenAI para gerar respostas automáticas baseadas nas mensagens recebidas.

## Estrutura do Projeto

### Arquivos Principais
1. **`extension.py`**: Gerencia a conexão com o MongoDB utilizando a biblioteca `flask_pymongo`.
2. **`main.py`**: Contém toda a lógica do bot, integrações com a Twilio e a API OpenAI, além de rotas definidas no Flask para receber e processar mensagens.
3. **`settings.py`**: Configurações gerais do projeto (não detalhado no código fornecido).

---

## Dependências

- **Flask**: Framework web usado para criar a API do bot.
- **Twilio**: Serviço de comunicação usado para enviar e receber mensagens via WhatsApp.
- **OpenAI**: Utilizado para geração de respostas automáticas com o modelo GPT-3.5.
- **Levenshtein**: Usado para calcular a distância entre palavras e encontrar correspondências aproximadas em entradas de usuários.
- **MongoDB**: Banco de dados NoSQL, gerenciado pelo `flask_pymongo`.

## Funcionalidades

### Envio de Mensagens com Twilio
O bot é capaz de enviar mensagens pelo WhatsApp utilizando a API do Twilio. A função `sendMessage` é responsável por enviar uma mensagem específica para um número de WhatsApp.

**Exemplo de uso da função:**
```python
sendMessage("Texto da mensagem", "whatsapp:+55XXXXXXXXX", "whatsapp:+14155238886")
```

### Resposta Automática com GPT-3.5
O bot utiliza o modelo GPT-3.5 da OpenAI para gerar respostas automatizadas com base nas mensagens recebidas.

### Reconhecimento de Mensagens e Comandos
O bot possui uma lista de palavras-chave válidas e responde adequadamente com base na entrada do usuário. Além disso, é possível definir respostas automáticas para mensagens específicas, como "sim", "não", e outros comandos pré-definidos.

### Rotas Flask
A aplicação define uma rota `/sms` que recebe requisições `POST` com os dados da mensagem recebida via Twilio. Esta rota processa a mensagem e retorna uma resposta apropriada.

**Exemplo de definição de rota:**
```python
@apbot.route("/sms", methods=["GET", "POST"])
def reply():
    msgt = request.form.get("Body")
    sen_num = request.form.get("From")
    me_num = request.form.get("To")
    # Lógica de resposta...
```

---

## Configuração e Execução

### Twilio
- Para integrar o WhatsApp com o Twilio, é necessário uma conta Twilio com a API habilitada para WhatsApp.
- **Credenciais Twilio**: Configure as variáveis `account_sid` e `auth_token` com os valores fornecidos pela Twilio.
  
**Exemplo de inicialização do cliente Twilio:**
```python
client = Client(account_sid, auth_token)
```

### OpenAI
- **Chave da API**: A OpenAI requer uma chave de API válida para gerar respostas. Esta chave pode ser configurada via variáveis de ambiente ou diretamente no código.

**Exemplo de chamada à API OpenAI:**
```python
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",  
  messages=[{"role": "assistant", "content": "Instruções..."}]
)
```

### MongoDB
- Utiliza o `flask_pymongo` para integração com o MongoDB, permitindo que informações relacionadas às interações com o usuário sejam armazenadas.

### Execução
Para executar o projeto, o servidor Flask é iniciado na porta configurada. Utilize o comando abaixo para rodar a aplicação:
```bash
python main.py
```

O Flask irá iniciar o servidor e o bot estará disponível para processar as mensagens recebidas.

---

## Funcionalidades Adicionais

- **Ajuda Automatizada**: O bot oferece uma lista de opções que o usuário pode selecionar para obter informações sobre a autoescola (localização, categorias, valores, etc.).
- **Respostas Pré-definidas**: Para certas palavras-chave, o bot responde com mensagens específicas, como informações sobre valores e prazos.

**Exemplo de resposta pré-definida:**
```python
if msgt == "1":
    msg = "R. Paulo Roberto Pinheiro, 70 – Guararapes, Fortaleza – CE, 60810-100"
    sendMessage(msg, sen_num, me_num)
```

---

## Melhoria da Experiência do Usuário

- **Correção de Erros de Digitação**: Utilizando a distância de Levenshtein, o bot pode sugerir correções caso o usuário tenha digitado uma palavra incorreta.
  
**Exemplo de uso do Levenshtein:**
```python
def find_closest_match(user_input, valid_words):
    closest_match = min(valid_words, key=lambda word: Levenshtein.distance(user_input, word))
    return closest_match
```

---

## Conclusão
Este projeto oferece uma solução completa para um chatbot que responde automaticamente a usuários do WhatsApp, integrado com Twilio e OpenAI, utilizando Python, Flask, e MongoDB. O bot pode ser personalizado para diferentes tipos de negócios, facilitando a comunicação com os clientes de forma automatizada.
