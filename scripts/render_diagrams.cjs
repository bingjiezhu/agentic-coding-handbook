// Render checked-in English SVGs. Set BROWSER_EXECUTABLE to use an installed browser.
const {chromium}=require('playwright');
const fs=require('node:fs/promises');const path=require('node:path');
const root=path.resolve(__dirname,'..');
(async()=>{
 const browser=await chromium.launch({headless:true,...(process.env.BROWSER_EXECUTABLE?{executablePath:process.env.BROWSER_EXECUTABLE}:{})});
 const page=await browser.newPage();await page.route('**/*',r=>r.abort());const reports=[];
 try{for(const file of (await fs.readdir(path.join(root,'assets/diagrams/en'))).filter(f=>f.endsWith('.svg')).sort()){
  const svg=await fs.readFile(path.join(root,'assets/diagrams/en',file),'utf8');
  await page.setContent('<html><style>html,body{margin:0;padding:0;background:#F3EDE3}svg{display:block}</style>'+svg+'</html>');await page.evaluate(()=>document.fonts.ready);
  const size=await page.$eval('svg',s=>({w:s.viewBox.baseVal.width,h:s.viewBox.baseVal.height}));await page.setViewportSize({width:size.w,height:size.h});
  const issues=await page.evaluate(()=>{const issues=[];for(const t of document.querySelectorAll('text')){
   const b=t.getBBox(),v=t.ownerSVGElement.viewBox.baseVal;
   if(b.x<0||b.y<0||b.x+b.width>v.width||b.y+b.height>v.height)issues.push('outside diagram: '+t.textContent);
   if(t.dataset.node){const g=t.closest('g');const x=+g.dataset.x,y=+g.dataset.y,w=+g.dataset.w,h=+g.dataset.h;
    if(b.x<x+6||b.x+b.width>x+w-6||b.y<y+3||b.y+b.height>y+h-3)issues.push('outside node: '+t.textContent);}
  }const ts=[...document.querySelectorAll('text')].map(t=>({s:t.textContent,b:t.getBBox()}));for(let i=0;i<ts.length;i++)for(let j=i+1;j<ts.length;j++){
   const a=ts[i],b=ts[j];if(Math.min(a.b.x+a.b.width,b.b.x+b.b.width)-Math.max(a.b.x,b.b.x)>1&&Math.min(a.b.y+a.b.height,b.b.y+b.b.height)-Math.max(a.b.y,b.b.y)>1)issues.push('overlap: '+a.s+' / '+b.s);
  }return issues;});
  if(issues.length){reports.push({key:file,...size,issues});continue;}
  const key=file.slice(0,-4);await page.pdf({path:path.join(root,'assets/diagrams/en',key+'.pdf'),width:size.w+'px',height:size.h+'px',printBackground:true,margin:{top:0,bottom:0,left:0,right:0}});
  await page.screenshot({path:path.join(root,'assets/diagrams/en',key+'.png')});reports.push({key,...size,issues});
 }}finally{await browser.close();}
 if(reports.some(r=>r.issues.length))throw new Error(reports.filter(r=>r.issues.length).map(r=>r.key+': '+r.issues.join('; ')).join('\n'));
 await fs.writeFile(path.join(root,'verification/diagram-checks.json'),JSON.stringify({method:'Playwright: text bounds, node bounds and pairwise text overlap',diagrams:reports},null,2)+'\n');console.log('All 13 English diagrams rendered and checked.');
})().catch(e=>{console.error(e.message);process.exit(1)});
