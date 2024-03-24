from typing import List
from tenacity import retry, wait_random_exponential, stop_after_attempt

# def generate_openai(client, model: str, messages: List) -> str:
#     completion = client.chat.completions.create(
#         model=model,
#         messages=messages,
#         max_tokens=100
#     )
#     return completion.choices[0].message.content.strip()
@retry(wait=wait_random_exponential(multiplier=1, max=40), stop=stop_after_attempt(3))
def chat_completion_request(client, messages, tools=None, tool_choice=None, model=GPT_MODEL):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=tools,
            tool_choice=tool_choice,
        )
        return response
    except Exception as e:
        print("Unable to generate ChatCompletion response")
        print(f"Exception: {e}")
        return e