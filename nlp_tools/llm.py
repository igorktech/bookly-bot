from logger import configure_logger
from tenacity import retry, wait_random_exponential, stop_after_attempt

logger = configure_logger()

GPT_MODEL = "gpt-3.5-turbo"


@retry(wait=wait_random_exponential(multiplier=1, max=40), stop=stop_after_attempt(5))
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
        logger.warning("Unable to generate ChatCompletion response")
        logger.warning(f"Exception: {e}")
        return e
