// Create a private comparison from actual preserved assessments, never decisions.
import fs from 'node:fs/promises';
import path from 'node:path';
import {Workbook} from '@oai/artifact-tool';
const folder=process.argv[2];
if(!folder)throw Error('Supply the private hash-named adjudication return directory');
const comparisons=JSON.parse(await fs.readFile(path.join(folder,'comparison.json'),'utf8'));
const summary=JSON.parse(await fs.readFile(path.join(folder,'summary.json'),'utf8'));
const keys=['adjudication_id','review_id','fixture_id','task_id','language','item_id'];
const derived=['reference_score','judge_score','first_pass_score','normalized_adjudication_score','reference_match','judge_match','changed_from_first_pass'];
const original=Object.keys(comparisons[0].as_returned).filter(k=>!keys.includes(k));
const fields=[...keys,...derived,...original,'returned_form_sha256'];
const numeric=new Set(derived.slice(0,4));
const matrix=[fields,...comparisons.map(r=>fields.map(k=>{
 const value=k==='returned_form_sha256'?summary.returned_form_sha256:derived.includes(k)?r[k]:r.as_returned[k];
 return value==null?'':numeric.has(k)?Number(value):value;
}))];
const workbook=Workbook.create();const sheet=workbook.worksheets.add('Comparison');
const range=sheet.getRangeByIndexes(0,0,matrix.length,fields.length);range.values=matrix;
range.format.font={name:'Arial',size:11};range.format.columnWidth=24;range.format.rowHeight=30;
sheet.getRangeByIndexes(0,0,1,fields.length).format={font:{bold:true,color:'#FFFFFF'},fill:'#31465A',wrapText:true,rowHeight:48};
sheet.showGridLines=false;workbook.recalculate();
const actual=range.values;
if(JSON.stringify(actual.map(r=>r.map(v=>v??'')))!==JSON.stringify(matrix))throw Error('Comparison cell fidelity failed');
const quote=v=>'"'+String(v??'').replaceAll('"','""')+'"';
const csv=actual.map(r=>r.map(quote).join(',')).join('\n')+'\n';
const output=path.join(folder,'POST_ADJUDICATION_COMPARISON.csv');
try{await fs.writeFile(output,csv,{mode:0o600,flag:'wx'});}
catch(error){if(error.code!=='EEXIST'||await fs.readFile(output,'utf8')!==csv)throw error;}
const preview=await workbook.render({sheetName:'Comparison',range:'A1:M8',scale:1,format:'png'});
await fs.writeFile(path.join(folder,'comparison_preview.png'),new Uint8Array(await preview.arrayBuffer()),{mode:0o600});
console.log('Seven source-linked comparison rows exported; original returned fields retained; ordinal half credit preserved.');
