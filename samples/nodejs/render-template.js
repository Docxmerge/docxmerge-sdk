const Docxmerge = new require("docxmerge")
const fs = require("fs")
const docxmerge = new Docxmerge("76db447cb9c64662b50bc1eda2ec10e0")
async function main() {
  const report = await docxmerge.renderTemplate(
    "aa0f3256-cb87-42ac-9f9e-ffabd4483b4d",
    "Hello world",
    { helloworld: "Hello world" },
  )
  report.content.pipe(fs.createWriteStream("report.pdf"))
}
main()
