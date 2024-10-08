import os
from twilio.rest import Client
from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
import Levenshtein
from openai import OpenAI
import openai
from dotenv import load_dotenv

load_dotenv()

client_openai = OpenAI(
    #defaults to os.environ.get("OPENAI_API_KEY")
    api_key= CHAT_API,
)

apbot = Flask(__name__)
def sendMessage(text : str, to: str, fromwwp: str):

    account_sid = ACCOUNT_SID,
    auth_token = AUTH_TOKEN
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        from_ ='whatsapp:+14155238886',
        body=text,
        to=to
        )
    print(message.sid)

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",  
  messages=[
    {"role": "assistant", "content": "Só me responda coisas relacionadas a AutoEscola Ari, localizada em fortaleza/Ceará. para checar as informações, consulte: https://autoescolaari.com "},
  ]
)



@apbot.route("/sms",methods = ["get","post"])
def reply():
    valid_words = ["oi","ola","olá", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "sim", "não", "autoescola", "bom dia", "boa tarde", "boa noite", "valor", "gostaria", "quero fazer", "como fazer", "como fazer?", "horários", "horário", "como começar", "como começar?", "eu quero começar", "eu queria começar", "começar autoescola", "tirar carteira", "entrar autoescola", "eu quero começar a autoescolar", "quero tirar a carteira", "quero dirigir", "quero começar a dirigir", "quero entrar", "eu quero entrar na escola", "como entrar na autoescola?", "como tirar a carteira?", "eu gostaria de iniciar", "professores", "vocês fazem pra tirar a carteira A ou B?", "carteira A", "carteira B", "qual o valor", "atendente", "atendimento", "professor", "quero falar com um atendente", "eu quero falar com um atendente", "quero falar com o atendente", "quero falar com a atendente", "quero atendimento", "solicito atendimento", "eu preciso falar com um atendente", "eu preciso falar com uma atendente", "eu preciso falar com um professor", "eu quero falar com um professor", "como eu falo com um atendente?", "como eu falo com um responsável?", "como eu falo com uma atendente?", "como eu falo com o atendente?", "quero ser atendido", "quero falar com alguem", "preciso falar com um atendente", "eu quero desconto", "como negociar a carteira de motorista", "eu quero tirar a carteira A e B", "preciso tirar a habilitação", "preciso de habilitação", "preciso habilitar", "preciso de habilitação", "habilitação", "setor de habilitação", "setor finaceiro", "carro", "moto", "A", "B", "A e B"]
    msgt = request.form.get("Body")
    msgt.lower()
    sen_num= request.form.get("From")
    me_num = request.form.get("To")
    print(msgt)
    print(sen_num)


    chat_completion = client_openai.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": msgt,
            }
        ],
        model="gpt-3.5-turbo",
    )

    print("Autoescola Ari")

    msg = chat_completion.choices[0].message.content

    sendMessage(msg, sen_num,me_num)
    
    
   
    if(msgt == "1" or msgt == "2" or msgt == "3" or msgt == "4" or msgt == "5" or msgt == "6" or msgt == "7" or msgt == "8"):
             secondReply(msgt)
    elif(msgt == "sim" or msgt == "Sim" or msgt == "s" or msgt == "ss" or msgt == "SIm" or msgt == "SIM" or msgt == "sIM" or msgt == "siM"):
            ajuda()
    
    elif(msgt == "não" or msgt == "Não" or msgt == "nao" or msgt == "Nao" or msgt == "n" or msgt == "nn"):
             msg = "Muito obrigado por estar conosco!!"
             sendMessage(msg, sen_num, me_num)
             msg = "Se precisar de algo a mais so mandar um olá!"
             sendMessage(msg, sen_num, me_num)
    elif(msgt == "experimental" or msgt == "test" or msgt == "Aula experimental" or msgt == "aula grátis" or msgt == "experimental grátis" or msgt == "teste grátis" or msgt == "aula de graça" or msgt == "Drive" or msgt == "teste experimental" or msgt == "aula teste" or msgt == "experimentar"):
          especifico(1)
          loop()
    elif(msgt == "Carteira tipo A" or msgt == "Carteira tipo B" or msgt == "A" or msgt == "B" or msgt == "Carteira tipo A e B" or msgt == "A e B" or msgt == "Quero tirar a carteira de carro" or msgt == "quero tirar a carteira de moto" or msgt == "carro" or msgt == "moto" or msgt == "Como tirar a carteira" or msgt == "como dirigir" or msgt == "Como entrar?" or msgt == "como começar?" or msgt == " Como iniciar" or msgt == "como começar" or msgt == "Como começo?"):
           especifico(2)
           loop()
    elif(msgt == "Seguro" or msgt == "seguro" or msgt =="vocês fazem seguro?" or msgt == "quero seguro" or msgt == "eu quero um seguro" or msgt == "onde arranjo um seguro?" or msgt == "preciso de seguro"):
          especifico(4)
          loop()
    elif(msgt == "Falar com atendente" or msgt == "Atendente" or msgt == "atendente" or msgt == "Vendedor" or msgt == "vendedor" or msgt == "Falar com vendedor" or msgt == "atendimento" or msgt == "Atendimento" or msgt == "Quero atendimento" or msgt == "quero atendimento" or msgt == "Quero falar com o atendente" or msgt == "quero falar com o atendente" or msgt == "Quero falar com a atendente" or msgt == "quero falar com a atendente"  or msgt == "Quero falar com o vendedor" or msgt == "quero falar com o vendedor" or msgt == "Quero falar com a vendedora" or msgt == "quero falar com a vendedora" or msgt == "Quero atendimento" or msgt == "quero atendimento" or msgt == "quero ser atendido" or msgt == "Quero ser atendido" or msgt == "atendente" or msgt == "atendimento" or msgt == "vendedor" or msgt == "quero falar com um atedente" or msgt == "eu quero falar com um atendente" or msgt == "quero falar com o atendente" or msgt == "quero falar com a atendente" or msgt =="quero atendimento" or msgt == "solicito atendimento" or msgt == "eu preciso falar com um atendente" or msgt == "eu preciso falar com uma atendente" or msgt == "eu preciso falar com um vendedor" or msgt == "eu quero falar com um vendedor" or msgt == "como eu falo com um atendente?" or msgt == "como eu falo com um vendedor?" or msgt == "como eu falo com uma atendente?" or msgt == "como eu falo com o atendente?" or msgt == "quero ser atendido" or msgt =="quero falar com alguem" or msgt == "preciso falar com um atendente" or msgt == "quero falar com um atendente"):
         especifico(5)
         loop()
    elif(msgt == "OI" or msgt == "Oi" or msgt == "oi" or msgt == "Olá" or msgt == "olá" or msgt == "Ola" or msgt == "ola" or msgt == "fala" or msgt == "opa" or msgt == "Fala" or msgt == "Opa" or msgt == "Bom dia" or msgt == "bom dia" or msgt == "bomdia" or msgt == "Boa tarde" or msgt == "boa tarde" or msgt == "boatarde" or msgt == "Bom tarde" or msgt == "bom tarde" or msgt == "bomtarde" or msgt == "Boa noite" or msgt == "boa noite" or msgt == "boanoite" or msgt == "Bom noite" or msgt == "bom noite" or msgt == "bomnoite" or msgt == "Boa dia" or msgt == "boa dia" or msgt == "boadia" or msgt == "Boadia" or msgt == "Bomtarde" or msgt == "Bomnoite" or msgt == "cuida" or msgt == "chama" or msgt == "agiliza" or msgt == "chama na alta" or msgt == "chama na alta garel" or msgt == "chama na alta garelzinho" or msgt == "garelzinho do mel"):
             intro()
             ajuda()
    
    elif(msgt == "setor adminstrativo" or msgt == "administrativo"):
          msg = "Segue o contato do setor administrativo:\n +55 85 99957-7909"
          sendMessage(msg,sen_num,me_num)
          loop()
    elif(msgt == "setor rh" or msgt == "rh" or msgt == "setor do rh"):
          msg = "Segue o contato do setor RH:\+55 85 99957-7909"
          sendMessage(msg,sen_num,me_num)
          loop()
    elif(msgt == "vendedor" or msgt == "vendedores" or msgt == "setor de vendedores" or msgt == "setor dos vendedores" or msgt == "setor de vendedor" or msgt == "setor dos vendedor" or msgt == "setor do vendedor" or msgt == "setor de vendas" or msgt == "setor de venda"):
           msg = "Segue o contato do setor de vendas:\+55 85 99957-7909"
           sendMessage(msg,sen_num,me_num)
           loop()
    elif(msgt == "4.1" or msgt == "41" or msgt == "4,1" or msgt == "4 1"):
          msg = "Nós temos o limite de três carros por dia venha nos vistitar e fazer o seu test drive"
          sendMessage(msg,sen_num,me_num)
          loop()
    elif(msgt == "4.2" or msgt == "42" or msgt == "4,2" or msgt == "4 2"):
          msg = "O nosso tempo limite é de 45 minutos por cada test drive"
          sendMessage(msg, sen_num, me_num)
          loop()
    elif(msgt == "5.1" or msgt == "51" or msgt == "5,1" or msgt == "5 1"):
          msg = "Nos recomendamos o seguro ..."
          sendMessage(msg, sen_num,me_num)
          loop()
    elif(msgt == "5.2" or msgt == "52" or msgt == "5,2" or msgt == "5 2"):
          msg = "Nós estamos focado completamente na venda de carros mas indicamos o seguro ... de extrema confiança!!"
          sendMessage(msg, sen_num,me_num)
          loop()
    
    else:
         sugestion = find_closest_match(msgt, valid_words) 
         msg = 'Desculpa nao entendi a sua duvida, voce quis dizer "'+sugestion+'"?\n(se a palavra for essa, redigite-a)' 
         sendMessage(msg, sen_num, me_num)         

def secondReply(inte):
    sen_num = request.form.get("From")
    me_num = request.form.get("To")
    if(inte == "onde vai acontecer o local?"):
        msg = "R. Paulo Roberto Pinheiro, 70 – Guararapes, Fortaleza – CE, 60810-100"
        sendMessage(msg, sen_num,me_num)
        loop()
    if(inte == "2"):
        msg = "Nós tiramos a sua carteira das categoria A e B"
        sendMessage(msg, sen_num,me_num)
        loop()
    if(inte == "3"):
        msg = "Vou te mostrar uma lista de valores de acordo com a categoria\n - Categoria A: 1200 R$\n - Categoria B: 1980 R$\nLembrando que parcelamos em até 10x sem juros e nesses valores já estão incluidas as taxas do detran!!"
        sendMessage(msg, sen_num,me_num)
        loop()
    if(inte == "4"):
        msg = "O processo de forma geral varia muito, mas a média de tempo até tirar a sua carteira é de 3 a 4 meses!!"
        sendMessage(msg, sen_num,me_num)
        loop()
    if(inte == "5"):
        msg = "O processo de renovação da carteira é diretamenete com o detran, mas você pode marcar aulas extras se estiver precisando basta falar com um de nossos atendentes!"
        sendMessage(msg, sen_num,me_num)
        loop()
    if(inte == "6"):
        msg = "Para fazer as provas teoricas apenas a sua identidade, mas para as aulas e prova pratica você precisara portar a sua LADV feita pela nossa auto escola!"
        sendMessage(msg, sen_num,me_num)
        loop()
    if(inte=="7"):
        msg = "Claro, para falar com um de nossos atendentes fixos basta adicionar o seguinte contato (85) 9999999999"
        sendMessage(msg, sen_num,me_num)
        loop()
        

def ajuda():
    sen_num = request.form.get("From")
    me_num = request.form.get("To")
    msg = "Como posso ajuda-lo?"
    sendMessage(msg, sen_num,me_num)
    msg = " 1 - Localização\n 2 - Quais categorias vocês tem?\n 3 - Qual o valor pra tirar a carteira?\n 4 - Quanto tempo demora pra tirar a carteira?\n 5 - Como funciona o processo de renovação?\n 6 - Quais documentos são necessarios para tirar a carteira?\n 7 - Falar com um atendente"
    sendMessage(msg, sen_num,me_num)

def intro():
    sen_num = request.form.get("From")
    me_num = request.form.get("To")

    msg = 'Olá, tudo bem?'
    sendMessage(msg, sen_num, me_num)
    msg = "Prazer eu sou o Ari e estou aqui pra ajudar"
    msg = 'Qual serviço você deseja?'
    sendMessage(msg, sen_num, me_num)
    

def loop():
    
    sen_num = request.form.get("From")
    me_num = request.form.get("To")

    msg = "Você precisa de mais alguma ajuda?\n (digite 'sim' ou 'não')"
    sendMessage(msg, sen_num, me_num)
    
def especifico(num):
     sen_num = request.form.get("From")
     me_num = request.form.get("To")

     if(num == 1):
          msg = "A nossas aulas práticas são diárias e você pode solicitá-las com um atendente."
          sendMessage(msg, sen_num, me_num)
         
     elif(num == 5):
          msg = "Me diga com qual setor você deseja falar:\n - Administrativo\n - RH\n - Professores\n"
          sendMessage(msg, sen_num, me_num)
          msg = "(digite uma das opções acima)"
          sendMessage(msg, sen_num, me_num)

def find_closest_match(user_input, valid_words):
   
    closest_match = min(valid_words, key=lambda word: Levenshtein.distance(user_input, word))
    return closest_match

    sendMessage(msg, sen_num, me_num)
if(__name__=="__main__"):
    port = int(os.environ.get("PORT", 5000))
    apbot.run(host='0.0.0.0', port=port)