#importing the OpenAI Python package, which allows us to interact with OpenAI's APIs.
import openai


#  setting the API key that will be used to authenticate the requests to the OpenAI API.
openai.api_key = "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"


# creating a new chat completion request and providing a prompt to the model in the form of a message from a user
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give me 3 ideas for apps I could build with openai apis "}])
print(completion.choices[0].message.content)




