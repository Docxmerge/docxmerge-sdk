import test = require("tape");
import fs = require("fs");
import Docxmerge = require("./");
import path = require("path");
import { isBuffer } from "util";
import { Stream } from "stream";
const fixturesDir = path.join(__dirname, "fixtures");
const tmpDir = path.join(process.cwd(), "tmp");
if (!fs.existsSync(tmpDir)) {
  fs.mkdirSync(tmpDir);
}
const apiKey = "8f22c304d0b44af2b03c2ad3d1aa5471";
const tenantId = "f60b0638-2f2e-4f92-b027-39cedfa06d4d";
const getDocxmerge = () => new Docxmerge(apiKey, "http://localhost:5030");
const getHelloworldTmpl = () =>
  fs.readFileSync(path.join(fixturesDir, "helloworld.docx"));
const saveFile = (data: Buffer, filename: string) =>
  fs.writeFileSync(path.join(tmpDir, filename), data);
const saveStream = (data: Stream, filename: string) =>
  data.pipe(fs.createWriteStream(path.join(tmpDir, filename)));
const templateName = "Hello world";
test("Merge template", async t => {
  const docxmerge = getDocxmerge();
  const docx = await docxmerge.mergeTemplate(
    tenantId,
    templateName,
    {
      hello_world: "Hello world.."
    },
    {},
    "DRAFT",
    1
  );
  t.true(docx);
  t.assert(isBuffer(docx));
  saveFile(docx, "helloworld_merged1.docx");
  t.end();
});

test("Merge file", async t => {
  const docxmerge = getDocxmerge();
  const docx = await docxmerge.mergeFile(tenantId, getHelloworldTmpl(), {
    hello_world: "Hello world."
  });
  t.true(docx);
  t.assert(isBuffer(docx));
  saveFile(docx, "helloworld_merged.docx");
  t.end();
});

test("Render file", async t => {
  const docxmerge = getDocxmerge();
  const pdf = await docxmerge.renderFile(tenantId, getHelloworldTmpl(), {
    hello_world: "Hello world."
  });
  saveFile(pdf, "helloworld_merged2.pdf");
  t.end();
});

test("Render template", async t => {
  const docxmerge = getDocxmerge();
  const { content } = await docxmerge.renderTemplate(
    tenantId,
    templateName,
    {
      hello_world: "Hello world."
    },
    {},
    "DRAFT",
    1
  );
  t.true(content);
  saveStream(content, "helloworld_merged.pdf");
  t.end();
});
test("Convert template", async t => {
  const docxmerge = getDocxmerge();
  const pdf = await docxmerge.convertTemplate(
    tenantId,
    templateName,
    {},
    "DRAFT",
    1
  );
  saveFile(pdf, "helloworld.pdf");
  t.true(pdf);
  t.assert(isBuffer(pdf));
  t.end();
});
test("Convert file", async t => {
  const docxmerge = getDocxmerge();
  const pdf = await docxmerge.convertFile(tenantId, getHelloworldTmpl());
  saveFile(pdf, "helloworld.pdf");
  t.true(pdf);
  t.assert(isBuffer(pdf));
  t.end();
});
