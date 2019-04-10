import test = require('tape');
import fs = require('fs');
import Docxmerge = require('./');
import path = require('path');
import { isBuffer } from 'util';
import { Stream } from 'stream';
const fixturesDir = path.join(process.cwd(), 'fixtures');
const tmpDir = path.join(process.cwd(), 'tmp');
if (!fs.existsSync(tmpDir)) {
  fs.mkdirSync(tmpDir);
}
const apiKey = 'BUl4qf5pKZZpaSWL9bIuz6bgjJ5ka0';
const getDocxmerge = () => new Docxmerge(apiKey, 'http://localhost:5101');
const getHelloworld = () =>
  fs.createReadStream(path.join(fixturesDir, 'helloworld.docx'));
const getHelloworldTmpl = () =>
  fs.readFileSync(path.join(fixturesDir, 'helloworld.docx'));
const saveFile = (data: Buffer, filename: string) =>
  fs.writeFileSync(path.join(tmpDir, filename), data);
const saveStream = (data: Stream, filename: string) =>
  data.pipe(fs.createWriteStream(path.join(tmpDir, filename)));
const templateName = 'carta-pago';
test('Transform template', async t => {
  const docxmerge = getDocxmerge();
  const pdf = await docxmerge.transformTemplate('hello-world');
  t.true(pdf);
  t.assert(isBuffer(pdf));
  saveStream(pdf, 'hello.pdf');
  t.end();
});
test('Transform file', async t => {
  const docxmerge = getDocxmerge();
  const pdf = await docxmerge.transformFile(getHelloworld());
  t.true(pdf);
  t.assert(isBuffer(pdf));
  saveStream(pdf, 'hello_2.pdf');
  t.end();
});
test('Merge template', async t => {
  const docxmerge = getDocxmerge();
  const pdf = await docxmerge.mergeTemplate('hello-world', {
    hello_world: 'Hello world 33'
  });
  t.true(pdf);
  t.assert(isBuffer(pdf));
  saveStream(pdf, 'hello_3.docx');
  t.end();
});
test('Merge file', async t => {
  const docxmerge = getDocxmerge();
  const pdf = await docxmerge.mergeFile(getHelloworld(), {
    hello_world: 'Hello world 44'
  });
  t.true(pdf);
  t.assert(isBuffer(pdf));
  saveStream(pdf, 'hello_4.docx');
  t.end();
});

test('Merge and transform template', async t => {
  const docxmerge = getDocxmerge();
  const pdf = await docxmerge.mergeAndTransformTemplate('hello-world', {
    hello_world: 'Hello world 55'
  });
  t.true(pdf);
  t.assert(isBuffer(pdf));
  saveStream(pdf, 'hello_3.pdf');
  t.end();
});
test('Merge and transform file', async t => {
  const docxmerge = getDocxmerge();
  const pdf = await docxmerge.mergeAndTransformFile(getHelloworld(), {
    hello_world: 'Hello world 66'
  });
  t.true(pdf);
  t.assert(isBuffer(pdf));
  saveStream(pdf, 'hello_4.pdf');
  t.end();
});
