from openai import OpenAI

client = OpenAI(
    api_key="<Your Key Here>"  # Replace with your actual API key
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",  # or gpt-3.5-turbo, gpt-4-turbo depending on your plan
    messages=[
        {"role": "system", "content": "You are a virtual assistant named JARVIS skilled in general tasks like Alexa and Google Cloud"},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
)

print(completion.choices[0].message.content)


