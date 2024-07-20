import google.generativeai as genai
import os

keyUSER = input("Insert your gemini key: ")

api_key = keyUSER

genai.configure(api_key=api_key)

def MainMenu():
    print("Bem vindo á sua AI:")
    print("---------------------")
    print("1. Construa sua AI(Configure sua AI parte a parte)")
    print("2. Usar AI (modo fácil, apenas utilizea sem complicações)")
    print("3. Fechar")
    print("-----------------------")
    print("\n")



def listModelsAI():
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
    

def BuildAI(model):

    listModelsAI()
    modeloAI = input("Digite qual modelo deseja utilizar: ")


    canditade_count = input("Quantas resposta deseja obter ao fazer uma pergunta? (Candidate count): ")
    temperature = input("Defina niveis de criatividade/originalidade da sua AI(Vaolores de 0,1 a 1)? (Temperature): ")


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

MainMenu()
option = int(input("Selecione sua opcção -> "))
match(option):
    case 1:
        model = BuildAI(model)

        chat = model.start_chat(history=[])

        prompt = input("Esperando prompt: ")

        while prompt != "Fim":
            response = chat.send_message(prompt)
            print(">> ", response.text, "\n")
            prompt = input("Esperando prompt: ")

    case 2:
        model = configAI()

        chat = model.start_chat(history=[])

        prompt = input("Esperando prompt: ")

        while prompt != "Fim":
            response = chat.send_message(prompt)
            print(">> ", response.text, "\n")
            prompt = input("Esperando prompt: ")


    case 3:
        exit()
    case _:
        print("Opcão inválida")


