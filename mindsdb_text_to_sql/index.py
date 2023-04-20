import os
import json
import requests
from lxml import etree
from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import UnstructuredURLLoader


class Index:
    def __init__(self):
        self.index = self._create_index()

    def _create_index(self):
        loader = self._load_documents()
        return VectorstoreIndexCreator().from_loaders([loader])

    def _get_urls(self, documents_filepath='config/documents.json'):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), documents_filepath), 'r') as documents_file:
            examples = json.loads(documents_file.read())

        for url, xpath in examples.items():
            page = requests.get(url)
            tree = etree.HTML(page.content)

            return ["https://docs.mindsdb.com/" + element.attrib['href'] for element in tree.xpath(xpath)]

    def _load_documents(self):
        urls = self._get_urls()
        return UnstructuredURLLoader(urls=urls)

    def query(self, query):
        return self.index.query(query)
