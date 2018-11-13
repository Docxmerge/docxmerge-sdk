from shutil import copyfile

from docxmerge_sdk.main import Docxmerge

if __name__ == '__main__':
    docxmerge = Docxmerge()
    o = docxmerge.render_file(open("../diploma.docx"), {
        "Enter your high school name:": "YOUR HIGH SCHOOL",
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
