import sys, torch, torchaudio as ta
from chatterbox.tts import ChatterboxTTS
P, out = sys.argv[1], sys.argv[2]
dev = "mps" if torch.backends.mps.is_available() else "cpu"
print("device", dev, flush=True)
m = ChatterboxTTS.from_pretrained(device=dev)
ref = f"{P}/voice/ref_af_heart.wav"
jobs = {1: ("NVIDIA's CEO just resigned. Effective immediately.", 0.6, 0.4),
        7: ("ATOM ZEE keeps things moving. Tasks tracked, reminders on time.", 0.6, 0.4)}
for i, (text, e, c) in jobs.items():
    w = m.generate(text, audio_prompt_path=ref, exaggeration=e, cfg_weight=c)
    ta.save(f"{out}/new{i}.wav", w.cpu(), m.sr)
    print("line", i, round(w.shape[-1] / m.sr, 2), "s", flush=True)
