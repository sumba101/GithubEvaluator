import openai


def response_gen(message: str, system_prompt: str, count: int):
    messages = []
    if count == 0:
        messages.append({
            "role": "system",
            "content": system_prompt
        })
    messages.append({
        "role": "user",
        "content": message
    })

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0
    ).choices[0].message

    messages.append(response)
    return response["content"]
