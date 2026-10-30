"""Write params/<pre>.json from the tuned fins stage (or body stage with --body): per species, its module and the exact PILOT_*
environment of its final render. build.py reproduces those sheets pixel for pixel from this file.
  python3 export_params.py <pre> [--body] [names...]      (merges into an existing params file)"""
import os, sys, json, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import v4env, tune
def main():
    args = sys.argv[1:]; pre = args[0]; stage = 'body' if '--body' in args else 'fins'; names = [a for a in args[1:] if not a.startswith('--')]
    dst = os.path.join(v4env.V4, 'params', pre + '.json'); P = json.load(open(dst)) if os.path.exists(dst) else {}
    for f in sorted(glob.glob(os.path.join(tune.work(pre, stage), f'{pre}_*_tune.json'))):
        j = json.load(open(f))
        if names and j['name'] not in names: continue
        p = dict(tune.START); p.update(j['params'])
        e = tune.env_for(pre, j['name'], p, '-', fins=(stage == 'fins'))
        P[j['name']] = dict(module=j['mod'], stage=stage, env={k: v for k, v in sorted(e.items()) if k.startswith('PILOT_') and k != 'PILOT_OUT'})
    json.dump(P, open(dst, 'w'), indent=1, sort_keys=True); print(len(P), 'species in', dst)
if __name__ == '__main__': main()
