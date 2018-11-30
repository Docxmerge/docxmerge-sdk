const fs = require("fs");
const Docxmerge = require("docxmerge");
const docxmerge = new Docxmerge(apikey)
const file = fs.readFileSync("invoice.docx")
async function main() {
  const report = await docxmerge.renderFile(file, {
    company: "Docxmerge",
    date: "01/01/2018",
    orders: [
      {
        description: "Description",
        qty: "4",
        price: "$10.00",
        total: "$40.00",
      },
      {
        description: "Description",
        qty: "4",
        price: "$10.00",
        total: "$40.00",
      },
    ],
    subtotal: "$80.00",
    tax: "$16.00",
    total: "$96.00",
  })
  fs.writeFileSync("invoice.pdf", report)
}
main()
