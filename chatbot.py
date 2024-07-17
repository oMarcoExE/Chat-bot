import google.generativeai as genai

keyUSER = input("Insert your gemini key: ")

api_key = keyUSER

genai.configure(api_key=api_key)

def listModelsAI():
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
    

def configAI():
    config = {
        "candidate_temperatue": 1,
        "temperature": 0.5,
    }

    seguranca = {
        "Harassment": "BLOCK_NONE",
        "Violence": "BLOCK_NONE",
        "Hate speech": "BLOCK_NONE",
        "Hate speech or offensive language": "BLOCK_ALL",
    }


listModelsAI()

