import openai

def set_openai_key(key):
    """Sets OpenAI key."""
    openai.api_key = key

from .text_to_sql import TextToSQL