const Docxmerge = require("../dist")
const fs = require("fs")
const path = require("path")
const { apikey, tenantId, endpoint } = require("./config")
const docxmerge = new Docxmerge(apikey, endpoint)
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
      fs.writeFileSync(path.join(__dirname, "out.pdf"), res.body)
    })
    .catch(err => {
      console.log(JSON.stringify(err))
    })
}
main()
