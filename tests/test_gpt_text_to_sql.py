import os
import unittest
from dotenv import load_dotenv

from mindsdb_text_to_sql import GPTTextToSQL

load_dotenv()


class TestGPTTextToSQL(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tts = GPTTextToSQL(os.environ.get("API_KEY"))

    def test_select_query(self):
        self.assertEqual(
            self.tts.convert_text_to_sql("Get the top 10 rows from the customer table of the databricks_datasource who earn a salary greater than 100000"),
            "SELECT * FROM databricks_datasource.customer\nWHERE salary > 100000\nLIMIT 10;",
        )