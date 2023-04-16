import openai

# Set OpenAI API key
openai.api_key = "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"

# Create an empty list to store conversation messages
messages = []

# Prompt user for chatbot type and add system message to messages list
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

# Print confirmation message
print("Your new assistant is ready!")

# Continue looping until user enters "quit()"
while True:
    message = input()  # Prompt user for message
    if message == "quit()":
        break  # Exit loop if user enters "quit()"
    
    # Add user message to messages list
    messages.append({"role": "user", "content": message})
    
    # Generate response using OpenAI API
    response = openai.Completion.create(
        engine="davinci",
        prompt=[{"text": msg["content"], "user": msg["role"]} for msg in messages],
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    # Extract generated response from API response and add to messages list
    reply = response.choices[0].text.strip()
    messages.append({"role": "assistant", "content": reply})
    
    # Print generated response
    print("\n" + reply + "\n")
