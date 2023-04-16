import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a financial experts that specializes in financial advice, investment and negotiation"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Financial Pro")

demo.launch(share=True)