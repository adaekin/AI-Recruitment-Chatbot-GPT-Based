import time
import gradio as gr
import yeni as ajan

def slow_echo(message, history):
    raw = ajan.runAgent(message)
    try:
        if raw.choices[0].message.content is not None:
            response = raw.choices[0].message.content #BUNU AJAN SCRIPTINE TAŞI
        else:
            response = "None"
    except:
        response = ""
    if response is None:
        response =""
        return
    if response is not None:
        for i in range(len(response)):
            time.sleep(0.005)
            yield  response[: i+1]
    else:
        response = "Bu konuda yardımcı olamıyorum."
        for i in range(len(response)):
            time.sleep(0.005)
            yield  response[: i+1]



gr.ChatInterface(
    fn=slow_echo,
    fill_height= 500,



).launch()
