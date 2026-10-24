#!/usr/bin/env python3
"""Standalone Matplotlib figures from an existing four-model analysis snapshot.

Does not calculate or change estimands. Undefined effects remain labelled NA.
The source report is provisional until independent human QA is completed.
"""
import argparse
import importlib.metadata
import json
from pathlib import Path

import prelim_four as four


def plot(report_path,out_dir):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    report=json.loads(report_path.read_text())
    if report.get('expected_cells')!=1884 or len(set(report['models']))!=4:
        raise RuntimeError('four-model preliminary report required')
    title=('SYNTHETIC TEST FIXTURE — no research findings' if report.get('synthetic_test_fixture') else
           'Preliminary 157-task four-model evaluation\nProvisional automated scores; independent human QA pending')
    out_dir.mkdir(parents=True,exist_ok=False)
    models=report['models'];effect=report['effects']['critical_omission_rate:bn-en']
    labels=models+['Equal-weight panel'];points=[effect['by_model'][m] for m in models]+[effect['estimate']]
    intervals=[effect['by_model_ci95'][m] for m in models]+[effect['ci95']]
    fig,ax=plt.subplots(figsize=(9,4.8))
    for i,(point,ci) in enumerate(zip(points,intervals)):
        if point is None or any(x is None for x in ci):ax.text(0,i,'NA',va='center')
        else:
            # Percentile intervals need not include the point estimate.
            ax.hlines(i,ci[0],ci[1],color='#2166ac',linewidth=2)
            ax.plot(point,i,'o',color='#2166ac')
    ax.axvline(0,color='gray',linewidth=.8);ax.set_yticks(range(len(labels)),labels)
    ax.invert_yaxis();ax.set_xlabel('Critical Omission Rate difference: Bengali − English')
    ax.set_title(title)
    fig.text(.02,.02,'95% domain-stratified task-cluster bootstrap intervals; positive = more Bengali omissions.',fontsize=8)
    fig.tight_layout(rect=(0,.04,1,1))
    for ext in ('png','pdf','svg'):fig.savefig(out_dir/('critical_omission_bn_en.'+ext),dpi=180)
    plt.close(fig)
    fig,ax=plt.subplots(figsize=(9,5))
    languages=('en','bn','bn_cs');colors=('#2166ac','#b2182b','#4d9221')
    for j,(lang,color) in enumerate(zip(languages,colors)):
        for i,model in enumerate(models):
            item=report['outcome_summary'][f'{model}:{lang}']['critical_omission_rate']
            value=item['mean'];x=i+(j-1)*.24
            if value is None:ax.text(x,.02,'NA',ha='center',fontsize=7)
            else:
                ax.bar(x,value,width=.22,color=color,label=lang.upper() if i==0 else None)
                ax.annotate(f"n={item['defined_cells']}",(x,value),xytext=(0,3),textcoords='offset points',ha='center',fontsize=7)
    ax.set_xticks(range(4),models,rotation=12,ha='right');ax.set_ylim(0,1.10)
    ax.set_ylabel('Descriptive mean Critical Omission Rate')
    ax.set_title(title)
    ax.legend();fig.text(.02,.02,'Response means with defined-cell counts. Paired effects above use the prespecified domain weighting.',fontsize=8)
    fig.tight_layout(rect=(0,.04,1,1))
    for ext in ('png','pdf','svg'):fig.savefig(out_dir/('critical_omission_by_language.'+ext),dpi=180)
    plt.close(fig)
    provenance={'source_report_sha256':four.digest(report_path),'plot_script_sha256':four.digest(Path(__file__)),
                'score_status':report['score_status'],'matplotlib_version':importlib.metadata.version('matplotlib'),
                'numpy_version':importlib.metadata.version('numpy'),
                'files_sha256':{p.name:four.digest(p) for p in sorted(out_dir.iterdir())}}
    (out_dir/'provenance.json').write_text(json.dumps(provenance,indent=2)+'\n')


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('report',type=Path);p.add_argument('--out-dir',type=Path,required=True)
    args=p.parse_args();plot(args.report,args.out_dir)
