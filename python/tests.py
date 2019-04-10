import json
import unittest
from docxmerge_sdk.main import Docxmerge

api_key = "BUl4qf5pKZZpaSWL9bIuz6bgjJ5ka0"
host = "http://localhost:5101"


class TestDocxmerge(unittest.TestCase):

    def test_transform_template(self):
        docxmerge = Docxmerge(api_key, host)
        docxmerge.transform_template("carta-pago")

    def test_transform_file(self):
        docxmerge = Docxmerge(api_key, host)
        docxmerge.transform_file(open("./data/helloworld.docx", 'rb'))

    def test_merge_template(self):
        docxmerge = Docxmerge(api_key, host)
        docxmerge.merge_template("carta-pago", data={})

    def test_merge_file(self):
        docxmerge = Docxmerge(api_key, host)
        docxmerge.merge_file(open("./data/helloworld.docx", 'rb'), data={'hello_world': 'Hello world1'})

    def test_merge_and_transform_template(self):
        docxmerge = Docxmerge(api_key, host)
        docxmerge.merge_and_transform_template("carta-pago", {'hello_world': 'Hello world1'})

    def test_merge_and_transform_file(self):
        docxmerge = Docxmerge(api_key, host)
        docxmerge.merge_and_transform_file(open("./data/helloworld.docx", 'rb'), {'hello_world': 'Hello world1'})


if __name__ == '__main__':
    unittest.main()
