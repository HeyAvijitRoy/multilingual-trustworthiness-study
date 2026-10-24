// Author the requested plain CSV forms with the spreadsheet artifact runtime.
import fs from 'node:fs/promises';
import path from 'node:path';
import {Workbook} from '@oai/artifact-tool';

const repo=process.cwd();
const packet=path.join(repo,'data/evaluation/reviews/v03_calibration_R1/adjudication');
const publicDir=path.join(repo,'data/evaluation/remediation/v03_R1_adjudication');
const input=JSON.parse(await fs.readFile(path.join(packet,'evidence/form_build_inputs.json'),'utf8'));
const quote=x=>'"'+String(x??'').replaceAll('"','""')+'"';
const jobs=[
 [packet,'R1_ADJUDICATION_FORM.csv',input.form_fields,input.form_rows],
 [packet,'POST_ADJUDICATION_COMPARISON_TEMPLATE.csv',input.comparison_fields,input.comparison_rows],
 [publicDir,'R1_ADJUDICATION_FORM_TEMPLATE.csv',input.form_fields,input.public_form_rows],
 [publicDir,'POST_ADJUDICATION_COMPARISON_TEMPLATE.csv',input.comparison_fields,input.public_comparison_rows],
];
for(const [dir,name,fields,rows] of jobs){
 const workbook=Workbook.create();const sheet=workbook.worksheets.add('Assessment');
 const matrix=[fields,...rows.map(r=>fields.map(k=>r[k]??''))];
 const range=sheet.getRangeByIndexes(0,0,matrix.length,fields.length);range.values=matrix;
 sheet.showGridLines=false;range.format.font={name:'Arial',size:11};
 range.format.columnWidth=26;range.format.rowHeight=30;
 sheet.getRangeByIndexes(0,0,1,fields.length).format={font:{bold:true,color:'#FFFFFF'},fill:'#31465A',wrapText:true,rowHeight:44};
 workbook.recalculate();
 const actual=range.values;
 if(JSON.stringify(actual.map(r=>r.map(x=>x??'')))!==JSON.stringify(matrix))throw Error('CSV cell fidelity failed');
 const output=actual.map(r=>r.map(quote).join(',')).join('\n')+'\n';
 await fs.writeFile(path.join(dir,name),output,{mode:dir===packet?0o600:0o644});
 if(name==='R1_ADJUDICATION_FORM.csv'){
   for(const [label,address] of [['identifiers','A1:I8'],['decisions','J1:O8'],['optional','P1:V8']]){
    const preview=await workbook.render({sheetName:'Assessment',range:address,scale:1,format:'png'});
    await fs.writeFile(path.join(repo,'.local/adjudication_toolchain',label+'.png'),new Uint8Array(await preview.arrayBuffer()));
   }
 }
 console.log(name+': seven rows, exact values and blank decision fields exported');
}
