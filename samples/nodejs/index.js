const fs = require("fs")
const Docxmerge = require("docxmerge")
const docxmerge = new Docxmerge(apikey)
const file = fs.readFileSync("./helloworld.docx")
async function main() {
  const report = await docxmerge.renderFile(file, {
    hello_world: "Hello world",
  })
  fs.writeFileSync("helloworld.pdf", report)
}
main()
