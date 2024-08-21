import google.generativeai as genai
import os

keyUSER = input("Insert your gemini key: ")
if keyUSER == "help":
    print("Não sabe como conseguir sua gemini key? Sem problemas!")
    print("Acesse google ai studio(https://ai.google.dev) \n faça login e clique em 'Get API Key'")
    keyUSER = input("Qual sua key -> ")
api_key = keyUSER

genai.configure(api_key=api_key)

def MainMenu():
    os.system('cls')
    print("Bem vindo á sua AI:")
    print("---------------------")
    print("1. Construa sua AI(Configure sua AI parte a parte)")
    print("2. Usar AI (modo fácil, apenas utilizea sem complicações)")
    print("3. Liste os modelos disponiveis")
    print("4. Fechar")
    print("-----------------------")
    print("\n")

    print("Comandos AI BOT")
    print("\n")
    print("Digite << Fim >> Para finalizar a conversa e voltar para o menu")

    return int(input("Selecione sua opcção -> "))


def listModelsAI():

    modelos = [
        "gemini-1.0-pro",
        "gemini-1.0-pro-latest",
        "gemini-1.0-pro-vision-latest",
        "gemini-1.5-flash",
        "gemini-1.5-flash-latest",
        "gemini-1.5-pro",
        "gemini-1.5-pro-latest",
        "gemini-pro",
        "gemini-pro-vision",
    ]
    for m, i in enumerate(modelos, start=1):
        print(f"{m}- {i}")

    #for m in genai.list_models():
    #    if 'generateContent' in m.supported_generation_methods:
    #        print(m.name)
    
def BuildAI(model):

    listModelsAI()
    optionModel = int(input("Digite qual n° de modelo deseja utilizar? (1, 2, 3...): "))
    match(optionModel):
        case 1: modeloAI = "gemini-1.0-pro"
        case 2: modeloAI = "gemini-1.0-pro-latest"
        case 3: modeloAI = "gemini-1.0-pro-vision-latest"
        case 4: modeloAI = "gemini-1.5-flash"
        case 5: modeloAI = "gemini-1.5-flash-latest"
        case 6: modeloAI = "gemini-1.5-pro"
        case 7: modeloAI = "gemini-1.5-pro-latest"
        case 8: modeloAI = "gemini-pro"
        case 9:  print("MODELO VISION DESABILITADO") 
                print("Modelo selecionado - gemini-1.5 pro") modeloAI = "gemini-pro-vision"
        case _: print("Modelo não encontrado.")

    print(modeloAI)

    canditade_count = int(input("Quantas resposta deseja obter ao fazer uma pergunta? (Candidate count): "))
    temperature = float(input("Defina niveis de criatividade/originalidade da sua AI(Vaolores de 0.1 a 1)? (Temperature): "))

    config = {
        "candidate_count": canditade_count,
        "temperature": temperature,
    }
    
    print("Configurações gerais setadas...")

    print("Sete as configurações de segurança (Responda tudo com BLOCK_NONE (para liberar) ou BLOCK_ALL (para bloquear))")
    Harassment = input("Comportamente de AI indesejado/não intencional: ")
    HATE = input("Odio, discurso de ódio etc: ")
    SEXUAL = input("Respostas com palavras sexuais ou coisas relacionadas: ")
    DANGEROUS = input("Respostas que possam ser consideradas perigosas: ")


    seguranca = {
        "Harassment": Harassment,
        "HATE": HATE,
        "SEXUAL": SEXUAL,
        "DANGEROUS": DANGEROUS,
    }

    model = genai.GenerativeModel(model_name= modeloAI,
                                generation_config= config,
                                safety_settings= seguranca)
    
    os.system("cls")
    print("Ai configurada com Sucesso.")
    input("Pressione Enter para usar sua AI")
    
    return model

def configAI():

    config = {
        "candidate_count": 1,
        "temperature": 0.5,
    }

    seguranca = {
        "Harassment": "BLOCK_NONE",
        "HATE": "BLOCK_NONE",
        "SEXUAL": "BLOCK_NONE",
        "DANGEROUS": "BLOCK_NONE",
    }

    model = genai.GenerativeModel(model_name= "gemini-1.0-pro",
                                generation_config= config,
                                safety_settings= seguranca) 
    
    return model

model = configAI()


option = 0
chat = model.start_chat(history=[])

while option != 3:
    option = MainMenu()
    match(option):
        case 1:
            model = BuildAI(model)

            prompt = input("Esperando prompt: ")

            while prompt != "Fim":
                response = chat.send_message(prompt)
                print(">> ", response.text, "\n")
                prompt = input("Esperando prompt: ")

        case 2:
            model = configAI()

            prompt = input("Esperando prompt: ")

            while prompt != "Fim":
                response = chat.send_message(prompt)
                print(">> ", response.text, "\n")
                prompt = input("Esperando prompt: ")
                
        case 3:
            listModelsAI()
            print("Modelos com 'pro (1.0/1.5) são sua versoes básicas'")
            print("Modelos com 'latest' são ós tal modelos em sua ultima versão")
            print("Modelos com flash, são suas versões rapidas e eficientes e leves")
            print("Modelos com 'vision' são versões que suportam upload de imagens/videos/arquivos pdfs")

            print("ps: Sistema ainda não suporta upload de arquivos (Modelo vision desabilitado)")

        case 4:
            exit()

        case _:
            print("Opcão inválida")