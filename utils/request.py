from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY')
)


def request_llm(model: str, prompt: str):
    """ Sends a message to an OpenAI Model
    Parameters:
        model (str): The name of the model
        prompt (str): The prompt to send
    Returns:
        None if error occurred, otherwise the response
    Notion:
        Please make sure the environment variable OPENAI_API_KEY exists,
        you can set it by changing the .env file
    """
    messages = [
        {'role': 'system', 'content': 'You\'re an expert at giving guidance to merchants.'},
        {'role': 'user', 'content': prompt}
    ]
    try:
        completion = client.chat.completions.create(
            model=model,
            messages=messages
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f'Error: {e}')
        return None
