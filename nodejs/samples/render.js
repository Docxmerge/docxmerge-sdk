const Docxmerge = require("../")
const fs = require("fs")
const path = require("path")

const docxmerge = new Docxmerge()
async function main() {
  docxmerge
    .renderFile(fs.readFileSync(path.join(__dirname, "diploma.docx")), {
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
      "Principal:": "Principal",
    })
    .then(async res => {
      fs.writeFileSync(path.join(__dirname, "out.pdf"), res)
    })
    .catch(err => {
      console.log(err.response.statusCode)
      console.log(err.response.body.toString())
    })
}
main()
