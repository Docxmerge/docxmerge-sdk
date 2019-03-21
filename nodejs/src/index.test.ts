import test = require("tape")
import fs = require("fs")
import Docxmerge = require("./")
import path = require("path")
import { isBuffer } from "util"
import { Stream } from "stream"
const fixturesDir = path.join(__dirname, "fixtures")
const tmpDir = path.join(process.cwd(), "tmp")
if (!fs.existsSync(tmpDir)) {
  fs.mkdirSync(tmpDir)
}
const apiKey = "580c2336ca7944a48626e70eeb243083"
const tenantId = "default"
const getDocxmerge = () => new Docxmerge(apiKey, "http://localhost:5030")
const getHelloworldTmpl = () =>
  fs.readFileSync(path.join(fixturesDir, "helloworld.docx"))
const saveFile = (data: Buffer, filename: string) =>
  fs.writeFileSync(path.join(tmpDir, filename), data)
const saveStream = (data: Stream, filename: string) =>
  data.pipe(fs.createWriteStream(path.join(tmpDir, filename)))
const templateName = "Hello world"
test("Render with tags", async t => {
  const docxmerge = getDocxmerge()
  const pdf = await docxmerge.convertTemplate(
    "default",
    "Hello world",
    {
      pec: "",
    },
    "DRAFT",
    1,
  )
  t.true(pdf)
  t.assert(isBuffer(pdf))
  saveFile(pdf, "pec.pdf")
  t.end()
})
test.only("Render url", async t => {
  const docxmerge = getDocxmerge()
  const pdf = await docxmerge.renderUrl(
    "landing",
    "https://minio.nextagilesoft.com/public/InvoiceTemplate.docx",
    {
      company: "Your Company Name",
      invid: "INVOICE",
      date: "01-01-2013",
      address: "Address",
      city: "City",
      state: "State",
      zip: "Zip",
      client_name: "Client Name",
      balance: "$0.00",
      notes: "Use this space for comments to your client.",
      orders: [
        {
          description: "Description",
          qty: "4",
          price: "9.99",
          total: "40",
        },
        {
          description: "Description",
          qty: "4",
          price: "9.99",
          total: "40",
        },
      ],
      subtotal: "$0.00",
      tax: "$0.00",
      total: "$0.00",
    },
  )
  t.true(pdf)
  t.assert(isBuffer(pdf))
  saveFile(pdf, "curr.pdf")
  t.end()
})
test("Merge template", async t => {
  const docxmerge = getDocxmerge()
  const docx = await docxmerge.mergeTemplate(
    tenantId,
    templateName,
    {
      hello_world: "Hello world..",
    },
    {},
    "DRAFT",
    1,
  )
  t.true(docx)
  t.assert(isBuffer(docx))
  saveFile(docx, "helloworld_merged1.docx")
  t.end()
})

test("Merge file", async t => {
  const docxmerge = getDocxmerge()
  const docx = await docxmerge.mergeFile(tenantId, getHelloworldTmpl(), {
    hello_world: "Hello world.",
  })
  t.true(docx)
  t.assert(isBuffer(docx))
  saveFile(docx, "helloworld_merged.docx")
  t.end()
})

test("Render file", async t => {
  const docxmerge = getDocxmerge()
  const pdf = await docxmerge.renderFile(tenantId, getHelloworldTmpl(), {
    hello_world: "Hello world.",
  })
  saveFile(pdf, "helloworld_merged2.pdf")
  t.end()
})

test("Render template", async t => {
  const docxmerge = getDocxmerge()
  const { content } = await docxmerge.renderTemplate(
    tenantId,
    templateName,
    {
      hello_world: "Hello world.",
    },
    {},
    "DRAFT",
    1,
  )
  t.true(content)
  saveStream(content, "helloworld_merged.pdf")
  t.end()
})
test("Convert template", async t => {
  const docxmerge = getDocxmerge()
  const pdf = await docxmerge.convertTemplate(
    tenantId,
    templateName,
    {},
    "DRAFT",
    1,
  )
  saveFile(pdf, "helloworld.pdf")
  t.true(pdf)
  t.assert(isBuffer(pdf))
  t.end()
})
test("Convert file", async t => {
  const docxmerge = getDocxmerge()
  const pdf = await docxmerge.convertFile(tenantId, getHelloworldTmpl())
  saveFile(pdf, "helloworld.pdf")
  t.true(pdf)
  t.assert(isBuffer(pdf))
  t.end()
})
