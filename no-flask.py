import aisuite as ai
client = ai.Client()

client.configure({
  "ollama" : {
    "timeout": 600,
  }
});

models = ["ollama:llama3.1"]

messages = [
    {"role": "system", "content": "Respond in Pirate English."},
    {"role": "user", "content": "Tell me a joke."},
]

for model in models:
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.75
    )
    print(response.choices[0].message.content)