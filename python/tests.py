import json
import unittest
from docxmerge_sdk import Docxmerge, ApiError

api_key = "26JZ5iPpD4U3b9z7lqkXeB2OGsbdF7"
host = "http://localhost:5101"


class TestDocxmerge(unittest.TestCase):

    def test_render_template(self):
        docxmerge = Docxmerge(api_key, host=host)
        docxmerge.render_template("hello_world2", data={
            "hello_world": "HOLA"
        }, conversion_type="PDF", version="latest")

    def test_render_file(self):
        docxmerge = Docxmerge(api_key, host=host)
        docxmerge.render_file(open("./data/helloworld.docx", 'rb'), data={'hello_world': 'Hello world1'},
                              conversion_type="PDF")

    def test_render_url(self):
        url = "https://api.docxmerge.com/api/v1/File/GetContenido?id=cdb9842d-5e38-4149-a06b-e1079a208fc3&download=true"
        docxmerge = Docxmerge(api_key, host=host)
        docxmerge.render_url(url, data={'hello_world': 'Hello world1'}, conversion_type="PDF")


if __name__ == '__main__':
    unittest.main()
