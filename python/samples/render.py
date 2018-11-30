from shutil import copyfile

from docxmerge_sdk.main import Docxmerge

if __name__ == '__main__':
    docxmerge = Docxmerge('06a468217a55439690c4eefbb94791e4', host='http://localhost:5030')
    o = docxmerge.render_file('de9a2bfd-86be-470d-a549-bd09fb1b1d2b', open("../diploma.docx"), {
        "Enter your high school name:": "YOUR HIGH SCHOOL111",
        "This certifies that:": "THIS CERTIFIES THAT",
        "Enter name:": "Name",
        "Certificate description:": "and is therefore awarded this",
        "Enter state:": "State",
        "Enter diploma:": "DIPLOMA",
        "Dated this:": "Dated this",
        "Enter day:": "Day",
        "Of:": "of",
        "Enter month:": "Month",
        "Superintendent:": "Superintendent",
        "Seal:": "SEAL",
        "Principal:": "Principal"
    })
    copyfile(o, "../out.pdf")
