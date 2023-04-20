import openai
from .text_to_sql import TextToSQL


def set_openai_key(key):
    """Sets OpenAI key."""
    openai.api_key = key