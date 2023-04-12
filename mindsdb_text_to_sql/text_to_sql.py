from .gpt import GPT


class TextToSQL:
    def __init__(self, engine='davinci', temperature=0.5, max_tokens=100, input_prefix="input: ", input_suffix="\n",
                 output_prefix="output: ", output_suffix="\n\n", append_output_prefix_to_query=False):
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

