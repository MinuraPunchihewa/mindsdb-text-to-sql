from .index import Index


class IndexTextToSQL:
    def __init__(self, api_key):
        self.index = Index(api_key)

    def convert_text_to_sql(self, text):
        return self.index.index.query(text)