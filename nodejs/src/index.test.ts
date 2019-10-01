import test = require("tape")
import fs = require("fs")
import mimeTypes = require("mime-types")
import Docxmerge = require("./")
import path = require("path")
import { isBuffer } from "util"
import { Stream } from "stream"
const fixturesDir = path.join(process.cwd(), "fixtures")
const tmpDir = path.join(process.cwd(), "tmp")
if (!fs.existsSync(tmpDir)) {
  fs.mkdirSync(tmpDir)
}
const apiKey = "26JZ5iPpD4U3b9z7lqkXeB2OGsbdF7"
const getDocxmerge = () =>
  new Docxmerge(apiKey, "tenant", "http://localhost:5101")
const getHelloworld = () =>
  fs.createReadStream(path.join(fixturesDir, "helloworld.docx"))
const getHelloworldTmpl = () =>
  fs.readFileSync(path.join(fixturesDir, "helloworld.docx"))
const saveFile = (data: Buffer, filename: string) =>
  fs.writeFileSync(path.join(tmpDir, filename), data)
const saveStream = (data: Stream, filename: string) =>
  data.pipe(fs.createWriteStream(path.join(tmpDir, filename)))
const templateName = "carta-pago"
test("Render template", async t => {
  const docxmerge = getDocxmerge()
  const pdf = await docxmerge.renderTemplate(
    "example-hello-world",

    {
      name: "James bond",
      logo: "https://docxmerge.com/assets/android-chrome-512x512.png",
    },
    "PDF",
    "latest",
  )
  t.true(pdf)
  // t.assert(isBuffer(pdf))
  const ext = mimeTypes.extension((pdf as any).headers["content-type"])
  saveStream(pdf, `hello_2.${ext || "pdf"}`)
  t.end()
})

test("Render file", async t => {
  const docxmerge = getDocxmerge()
  const pdf = await docxmerge.renderFile(
    getHelloworld(),
    {
      hello_world: "Hello world 66",
    },
    "HTML",
  )
  t.true(pdf)
  // t.assert(isBuffer(pdf))
  const ext = mimeTypes.extension((pdf as any).headers["content-type"])
  saveStream(pdf, `hello_world.${ext || "pdf"}`)
  t.end()
})

test("Render url", async t => {
  try {
    const docxmerge = getDocxmerge()
    const pdf = await docxmerge.renderUrl(
      "https://api.docxmerge.com/api/v1/File/GetContenido?id=cdb9842d-5e38-4149-a06b-e1079a208fc3&download=true",
      {
        hello_world: "Hello world 66",
      },
      "PDF",
    )
    t.true(pdf)
    // t.assert(isBuffer(pdf))
    const ext = mimeTypes.extension((pdf as any).headers["content-type"])
    saveStream(pdf, `hello_world_url.${ext || "pdf"}`)
  } catch (e) {
    saveStream(e, `hello_world_url.json`)
    console.log(e)
  }
  t.end()
})
