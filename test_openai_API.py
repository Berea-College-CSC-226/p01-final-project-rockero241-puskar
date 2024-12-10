from openai import OpenAI
import os
api_key = os.environ.get("OPENAI_API_KEY")

client = OpenAI(api_key = api_key)

message = input("\nAsk Chatgpt something: ")


completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a wise life coach who gives simple, straightforward and practical advice but make sure to be relevant to what the user journaled today"},
        {
            "role": "user",
            "content": message
        }
    ]
)

print("\nCHATGPT: ",completion.choices[0].message.content)