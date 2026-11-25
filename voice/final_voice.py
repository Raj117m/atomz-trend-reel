import json, subprocess, sys
import numpy as np, soundfile as sf
P = sys.argv[1]; TMP = f"{P}/voice/trim_work"
SR = 48000
KEY = {1, 7, 9, 10}; SETUP, KEYT = 1.12, 1.05
OVERRIDE = {1: f"{TMP}/new1.wav", 7: f"{TMP}/new7.wav"}
t = json.load(open(f"{P}/voice/mps_timing.json"))
lines = [x.strip() for x in open(f"{P}/lines.txt") if x.strip()]
def ff(args):
    r = subprocess.run(["ffmpeg", "-y", "-v", "error", *args], capture_output=True, text=True)
    if r.returncode: raise SystemExit(r.stderr[-300:])
def gap(s): return np.zeros(int(s * SR), dtype=np.float32)
parts, starts, ends, pieces = [], [], [], []
cur = 0.0
for i, l in enumerate(t["lines"], 1):
    seg = f"{TMP}/f_seg{i:02d}.wav"
    if i in OVERRIDE:
        ff(["-i", OVERRIDE[i], "-ar", str(SR), "-ac", "1", seg])
    else:
        ff(["-ss", f"{max(0, l['start'] - 0.05):.3f}", "-to", f"{l['end'] + 0.05:.3f}", "-i", f"{P}/voice/mps_voice.wav", "-ar", str(SR), "-ac", "1", seg])
    tr = f"{TMP}/f_trim{i:02d}.wav"
    ff(["-i", seg, "-af", "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.02,areverse,"
        "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.02,areverse", tr])
    fx = f"{TMP}/f_fx{i:02d}.wav"
    ff(["-i", tr, "-af", f"atempo={KEYT if i in KEY else SETUP}", fx])
    a, _ = sf.read(fx, dtype="float32")
    pause = 0.2 if i == 1 else (0.35 if i in (7, 10) else 0.2)
    if i == 1:
        parts.append(gap(0.2)); cur += 0.2
    else:
        parts.append(gap(pause)); cur += pause
    starts.append(cur); parts.append(a); cur += len(a) / SR; ends.append(cur)
    pieces.append(a)
parts.append(gap(0.4))
full = np.concatenate(parts)
raw = f"{TMP}/final_raw.wav"; sf.write(raw, full, SR)
out = f"{P}/assets/voice.wav"
ff(["-i", raw, "-af", "acompressor=threshold=-18dB:ratio=2.5:attack=8:release=180:makeup=2,loudnorm=I=-16:TP=-1.5:LRA=9", "-ar", "48000", "-ac", "1", out])
# timings: words spread across each line's speech span
words = []
for i, (s, e) in enumerate(zip(starts, ends), 1):
    ws = lines[i - 1].split(); wt = [len(w) + 1.5 for w in ws]; tot = sum(wt); c = s
    for w, x in zip(ws, wt):
        d = (e - s) * x / tot
        words.append({"text": w, "start": round(c, 3), "end": round(c + d, 3)}); c += d
timing = {"lines": [{"start": round(s, 3), "end": round(e, 3)} for s, e in zip(starts, ends)],
          "words": words, "emotions": t.get("emotions", []), "mode": "tts",
          "voice": "Chatterbox (cloned from af_heart reference), trimmed",
          "speed": "atempo 1.12 setup / 1.05 key", "total": round(len(full) / SR + 1.0, 3)}
json.dump(timing, open(f"{P}/voice/timing.json", "w"), indent=2)
print("total", timing["total"], "s")
for i, (s, e) in enumerate(zip(starts, ends), 1): print(i, round(e - s, 2), "s", lines[i - 1][:55])
