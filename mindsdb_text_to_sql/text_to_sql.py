from .gpt import GPT, set_openai_key


class TextToSQL:
    def __init__(self, api_key, engine='text-davinci-003', temperature=0, max_tokens=150, input_prefix="input: ", input_suffix="\n",
                 output_prefix="", output_suffix="", append_output_prefix_to_query=False):
        set_openai_key(api_key)

        self.gpt = GPT(
            engine,
            temperature,
            max_tokens,
            input_prefix,
            input_suffix,
            output_prefix,
            output_suffix,
            append_output_prefix_to_query
        )

        self.gpt.add_examples()

    def convert_text_to_sql(self, text):
        return self.gpt.get_top_reply(text)

