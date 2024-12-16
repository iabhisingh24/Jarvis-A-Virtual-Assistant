from openai import OpenAI
# client = OpenAI()




client = OpenAI(
    api_key= "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"
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in task like Alexa and Google Cloud"},
        {
            "role": "user","content": "Who is Tom Cruise."   
        }
    ]
)

print(completion.choices[0].message) 