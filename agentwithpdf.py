import os
from openai import AzureOpenAI
from Prompt.prompt import SYSTEMPROMPT, IYIORNEKCV1, KOTUORNEKCV2
from Prompt.sifreler import apikey
import pdfdeneme as _pdf

endpoint = "https://azureyza.cognitiveservices.azure.com/"
model_name = "gpt-4.1"
deployment = "gpt-4.1"

subscription_key = apikey
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)



tools = [{
        "type": "function",
        "function": {
            "name": "test_fonksiyonu", # BOŞLUK KABUL ETMİYOR
            "description": "fizikle alakalı işlem yapacağım",
            "parameters": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "The city name, e.g. San Francisco",
                    },
                },
                "required": ["message"],
            },
        }
        
        
    },
    {
        "type": "function",
        "function": {
            "name": "test_fonksiyonu2", # BOŞLUK KABUL ETMİYOR
            "description": "matematik işlemi yapacağım",
            "parameters": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "blablabla",
                    },
                },
                "required": ["message"],
            },
        }
        
        
    }]

def testfonk():
    return "Geldi"

def testfonk2():
    return "Geldi2"

def runAgent(user_Input:str):
    _response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": SYSTEMPROMPT,
            },
            {
                "role": "user",
                "content": user_Input,
            }
        ],
        max_completion_tokens=13107,
        temperature=1.0,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        tools= tools,
        tool_choice="auto",
        model=deployment
    )
    return _response

_raw = runAgent(_pdf.extract_text_from_pdf("cv3.pdf"))

print(_raw.choices[0].message.content)