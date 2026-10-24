#!/usr/bin/env python3
"""Export the local preparation draft to ACM LaTeX; no PDF-ready claim."""
import hashlib
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
D=ROOT/'manuscript/acm_trust2027'
KEYS={1:'pyramid2004',2:'mega2023',3:'helm2023',4:'agreement2008',5:'selfpreference2024'}


def escape(text):
    chars={'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_',
           '{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}',
           '≥':r'\ensuremath{\geq}','−':r'\ensuremath{-}','×':r'\ensuremath{\times}',
           '–':'--','—':'---','“':'``','”':"''",'‘':"`",'’':"'"}
    return ''.join(chars.get(c,c) for c in text)


def inline(text):
    parts=re.split(r'(`[^`]+`|\*\*[^*]+\*\*|\*[^*]+\*|\[[1-5]\])',text)
    out=[]
    for p in parts:
        if p.startswith('`') and p.endswith('`'):out.append(r'\texttt{'+escape(p[1:-1])+'}')
        elif p.startswith('**') and p.endswith('**'):out.append(r'\textbf{'+escape(p[2:-2])+'}')
        elif p.startswith('*') and p.endswith('*'):out.append(r'\emph{'+escape(p[1:-1])+'}')
        elif re.fullmatch(r'\[[1-5]\]',p):out.append(r'\cite{'+KEYS[int(p[1:-1])]+'}')
        else:out.append(escape(p))
    return ''.join(out)


def body(text):
    lines=text.strip().splitlines();out=[];i=0
    while i<len(lines):
        line=lines[i]
        if line=='$$':
            end=lines.index('$$',i+1);out.extend([r'\[','\n'.join(lines[i+1:end]),r'\]']);i=end+1;continue
        if line.startswith('|'):
            table=[]
            while i<len(lines) and lines[i].startswith('|'):
                cells=[x.strip() for x in lines[i].strip('|').split('|')]
                if not all(re.fullmatch(r'[-: ]+',x) for x in cells):table.append(cells)
                i+=1
            out.extend([r'\begin{table*}[t]',r'\caption{Completed automated calibration; the safety-related gate remains failed.}',r'\centering\small',r'\begin{tabular}{p{0.29\textwidth}p{0.26\textwidth}p{0.22\textwidth}p{0.12\textwidth}}',r'\toprule'])
            for n,row in enumerate(table):
                out.append(' & '.join(inline(c) for c in row)+r' \\')
                if n==0:out.append(r'\midrule')
            out.extend([r'\bottomrule',r'\end{tabular}',r'\end{table*}']);continue
        if line.startswith('### '):
            title=re.sub(r'^\d+(?:\.\d+)*\.?\s+','',line[4:]);out.append(r'\subsection{'+escape(title)+'}')
        elif line:out.append(inline(line))
        else:out.append('')
        i+=1
    return '\n'.join(out)


def render():
    source=D/'MANUSCRIPT.md';text=source.read_text();sections=re.split(r'^## ',text,flags=re.M)
    title=text.splitlines()[0][2:];blocks={part.split('\n',1)[0]:part.split('\n',1)[1] for part in sections[1:]}
    abstract=blocks.pop('Abstract');blocks.pop('References')
    out=[f'% Preparation export. Canonical Markdown SHA256: {hashlib.sha256(source.read_bytes()).hexdigest()}',
         '% Not compiled or page/font checked; no submission-ready claim.',
         r'\documentclass[sigconf,review,anonymous]{acmart}',r'\setcopyright{none}',
         r'\settopmatter{printacmref=false}',r'\acmDOI{}',r'\acmISBN{}',
         r'\title{'+escape(title)+'}',r'\begin{document}',r'\begin{abstract}',body(abstract),r'\end{abstract}',
         r'\keywords{multilingual evaluation, critical omission, required information units, Bengali, calibration, assurance}',
         r'\maketitle',r'\noindent\textbf{Preparation draft, October 24, 2026.} Raw generation in progress; production scoring and inferential findings pending. Calibration gate not passed.']
    for name,content in blocks.items():
        if name.startswith('GenAI usage'):
            out.append(r'\section*{GenAI Usage Disclosure --- Preparation Draft}')
        else:
            name=re.sub(r'^\d+\.\s+','',name);out.append(r'\section{'+escape(name)+'}')
        out.append(body(content))
    out.extend([r'\bibliographystyle{ACM-Reference-Format}',r'\bibliography{references}',r'\end{document}'])
    (D/'main.tex').write_text('\n\n'.join(out)+'\n')

if __name__=='__main__':render()
