import google.generativeai as genai

keyUSER = input("Insert your gemini key: ")

api_key = keyUSER

genai.configure(api_key=api_key)

def listModelsAI():
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
    

def configAI(modeloAI):
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

    model = genai.GenerativeModel(model_name= modeloAI,
                                generation_config= config,
                                safety_settings= seguranca) 
    
    return model



listModelsAI()
modeloAI = input("Digite qual modelo deseja utilizar: ")

model = configAI(modeloAI)

response = model.generate_content("Me explique em 3 paragrafos LLM")
print(response.text)
