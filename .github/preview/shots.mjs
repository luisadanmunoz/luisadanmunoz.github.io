import { chromium } from 'playwright';
import fs from 'node:fs';
const base = 'http://127.0.0.1:4000';
const out = process.argv[2] || 'shots';
fs.mkdirSync(out, { recursive: true });
const pages = [
  ['home', '/'], ['articulos', '/articulos/'], ['azure', '/articulos/azure/'], ['ia', '/articulos/ia/'],
  ['noticias', '/articulos/noticias/'], ['recursos', '/recursos/'], ['recursos-networking', '/recursos/networking/'],
  ['recurso-vnet', '/recursos/networking/virtual-network/'], ['sobre-mi', '/sobre-mi/'], ['privacidad', '/privacidad/'],
  ['404', '/404.html'],
];
const vps = { se: { width: 375, height: 667, isMobile: true, hasTouch: true, deviceScaleFactor: 2 }, desk: { width: 1280, height: 800 }, mob: { width: 390, height: 844, isMobile: true, hasTouch: true, deviceScaleFactor: 2 } };
const browser = await chromium.launch();
{ const c = await browser.newContext(); const p = await c.newPage(); await p.goto(base + '/articulos/'); const h = await p.getAttribute('.post-row', 'href'); pages.push(['post', h]); await c.close(); }
const report = [];
for (const [vk, vp] of Object.entries(vps)) {
  const ctx = await browser.newContext({ viewport: { width: vp.width, height: vp.height }, isMobile: !!vp.isMobile, hasTouch: !!vp.hasTouch, deviceScaleFactor: vp.deviceScaleFactor || 1 });
  const page = await ctx.newPage();
  for (const [name, path] of pages) {
    const r = await page.goto(base + path, { waitUntil: 'networkidle' }).catch(e => null);
    await page.waitForTimeout(400);
    const info = await page.evaluate(() => ({
      overflowX: document.documentElement.scrollWidth - window.innerWidth,
      height: document.documentElement.scrollHeight,
      text: document.body.innerText.length,
      toc: (() => { const t = document.querySelector('.toc'); const a = document.querySelector('#articulo'); if (!t || t.hidden || !a) return null; return { tocTop: Math.round(t.getBoundingClientRect().top + scrollY), artTop: Math.round(a.getBoundingClientRect().top + scrollY), tocLeft: Math.round(t.getBoundingClientRect().left) }; })(),
      navRows: (() => { const n = document.querySelector('.nav'); if (!n) return null; const tops = new Set([...n.children].map(c => Math.round(c.getBoundingClientRect().top))); return tops.size; })(),
    }));
    report.push({ vk, name, status: r && r.status(), ...info });
    await page.screenshot({ path: `${out}/${vk}-${name}.png`, fullPage: true });
  }
  // estados: menús abiertos y filtro
  await page.goto(base + '/', { waitUntil: 'networkidle' });
  for (const [i, sel] of [[1, '.nav details:nth-of-type(1) summary'], [2, '.nav details:nth-of-type(2) summary']]) {
    const el = await page.$(sel);
    if (el) { await el.click(); await page.waitForTimeout(300); await page.screenshot({ path: `${out}/${vk}-menu${i}.png` }); await el.click(); }
  }
  await page.goto(base + '/', { waitUntil: 'networkidle' });
  const cb = await page.$('.cta .consent input');
  if (cb) { await cb.scrollIntoViewIfNeeded(); await page.screenshot({ path: `${out}/${vk}-cta-off.png` }); await cb.click(); await page.waitForTimeout(150); await page.screenshot({ path: `${out}/${vk}-cta-on.png` }); }
  await page.goto(base + '/articulos/ia/', { waitUntil: 'networkidle' });
  const f = await page.$('.filter[data-filter]:not([data-filter="*"])');
  if (f) { await f.click(); await page.waitForTimeout(300); await page.screenshot({ path: `${out}/${vk}-filtro.png`, fullPage: true }); }
  await ctx.close();
}
fs.writeFileSync(`${out}/report.json`, JSON.stringify(report, null, 2));
await browser.close();
