#Groq test
import os
from groq import Groq
client = Groq(
    # This is the default and can be omitted
    api_key="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",
)
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of low latency LLMs",
        }
    ],
    model="llama3-8b-8192",
)
print(chat_completion.choices[0].message.content)

# export GROQ_API_KEY=<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>