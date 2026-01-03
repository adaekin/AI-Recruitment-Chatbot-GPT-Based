import os
from openai import AzureOpenAI
from Prompt.prompt import SYSTEMPROMPT, IYIORNEKCV1, KOTUORNEKCV2, TAKECVPROMPT
from Prompt.sifreler import apikey
import pdfdeneme as _pdf
import json

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
            "name": "read_pdf", # BOŞLUK KABUL ETMİYOR
            "description": "Özgeçmiş bilgilerini PDF'den çekeceğim.",
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

def read_pdf(agent_Input:str):
    print("TOOL ÇALIŞTIRILDI")
    cvPDF = _pdf.extract_text_from_pdf(agent_Input)
    return cvPDF



def runAgent(user_Input:str):
    _response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": SYSTEMPROMPT +"" + TAKECVPROMPT,
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
    # print(_response.choices[0].message.tool_calls[0].function.name)
    # try:
    #     print(_response.choices[0].message.tool_calls[0].function.name)
    # except:
    #     print("No tool called")
    try:
        if (_response.choices[0].message.tool_calls[0].function.name == "read_pdf"):
            js = json.loads(_response.choices[0].message.tool_calls[0].function.arguments)
            folderName = js["message"]
            print(read_pdf(folderName))
            cv = read_pdf(folderName)
            return runAgent(cv)
    except:
        print("no tool called")

    return _response.choices[0].message.content