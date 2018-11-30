from shutil import copyfile

from docxmerge_sdk.main import Docxmerge

if __name__ == '__main__':
    docxmerge = Docxmerge()
    o = docxmerge.render_file(open("./helloworld.docx",encoding='utf-8'), {
        "hello_world": "Hello world"
    })
    copyfile(o, "./helloworld.pdf")
