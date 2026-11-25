import json, subprocess, sys
import numpy as np, soundfile as sf
P = sys.argv[1]; src = sys.argv[2]; out = sys.argv[3]; tmp = sys.argv[4]
t = json.load(open(f"{P}/voice/mps_timing.json"))
lines = [x.strip() for x in open(f"{P}/lines.txt") if x.strip()]
KEY = {1, 7, 9, 10}                      # key lines: at most 1.05x
SETUP_MAX, KEY_MAX = 1.12, 1.05
SR = 48000
OVERRIDE = {1: f"{P}/voice/trim_work/new1.wav", 7: f"{P}/voice/trim_work/new7.wav"}
def ff(args):
    r = subprocess.run(["ffmpeg", "-y", "-v", "error", *args], capture_output=True, text=True)
    if r.returncode: raise SystemExit(r.stderr[-300:])
pieces = []
for i, l in enumerate(t["lines"], 1):
    seg = f"{tmp}/seg{i:02d}.wav"
    if i in OVERRIDE:
        ff(["-i", OVERRIDE[i], "-ar", str(SR), "-ac", "1", seg])
    else:
        ff(["-ss", f"{max(0, l['start'] - 0.05):.3f}", "-to", f"{l['end'] + 0.05:.3f}", "-i", src, "-ar", str(SR), "-ac", "1", seg])
    trimmed = f"{tmp}/trim{i:02d}.wav"
    ff(["-i", seg, "-af", "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.02,areverse,"
        "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.02,areverse", trimmed])
    tempo = KEY_MAX if i in KEY else SETUP_MAX
    fx = f"{tmp}/fx{i:02d}.wav"
    ff(["-i", trimmed, "-af", f"atempo={tempo}", fx])
    a, _ = sf.read(fx, dtype="float32")
    pieces.append((i, a, tempo))
gap = lambda s: np.zeros(int(s * SR), dtype=np.float32)
parts = []
for i, a, tempo in pieces:
    pause = 0.35 if i in (7, 10) else 0.20   # 350 ms before ATOM ZEE (line 7) and before the final line (10)
    if i == 1: parts.append(gap(0.2))
    else: parts.append(gap(pause))
    parts.append(a)
full = np.concatenate(parts + [gap(0.4)])
sf.write(out, full, SR)
dur = len(full) / SR
print("total before finish", round(dur, 2))
for i, a, tempo in pieces: print(i, round(len(a) / SR, 2), "s at", tempo)
