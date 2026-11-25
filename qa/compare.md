# Grammar check: atomz-trend-reel.mp4

```
1080x1920 @ 30.0 fps, 38.17 s
shots: 19 (4.71 changes per 10 s), length median 1.9 s [1.1-4.8], hard-cut share 0.94
visual beats: 4.97 per 10 s, gap median 1.8 s
ground: 18 changes, hold median 1.9 s, plain ground fills 67% of the frame
grounds by time: #ff6060 23.2s, #f0f0f0 15.0s
palette: #edeae7 41%, #fc595e 40%, #fc7176 13%, #191427 2%, #a9464a 1%, #e47233 1%, #47666d 1%, #a9a7ab 0%
saturation 0.371, brightness 0.935, flat share 0.952
motion: median 0.0098, p90 0.0375, static 7% of the time
audio: -13.0 LUFS, peak -1.4 dBTP, silent 0.14, no steady beat found
```

## Against r1: Video by kurzgesagt

| axis | measure | ours | reference | verdict |
| --- | --- | --- | --- | --- |
| pace | visual beats per 10 s | 4.97 | 2.94 | off |
| pace | gap between beats, median s | 1.8 | 2.65 | near |
| pace | shot length, median s | 1.9 | 10.2 | off |
| pace | hard-cut share of shot changes | 0.94 | None | n/a |
| ground | background hold, median s | 1.9 | 10.2 | off |
| ground | plain ground share of frame | 0.668 | 0.356 | off |
| motion | motion, median | 0.0098 | 0.0064 | near |
| motion | motion, p90 | 0.0375 | 0.0433 | ok |
| motion | static share of time | 0.066 | 0.079 | ok |

## Against r2: Video by kurzgesagt

| axis | measure | ours | reference | verdict |
| --- | --- | --- | --- | --- |
| pace | visual beats per 10 s | 4.97 | 4.16 | ok |
| pace | gap between beats, median s | 1.8 | 1.95 | ok |
| pace | shot length, median s | 1.9 | 1.75 | ok |
| pace | hard-cut share of shot changes | 0.94 | 0.48 | near |
| ground | background hold, median s | 1.9 | 1.25 | near |
| ground | plain ground share of frame | 0.668 | 0.462 | near |
| motion | motion, median | 0.0098 | 0.0151 | ok |
| motion | motion, p90 | 0.0375 | 0.0589 | ok |
| motion | static share of time | 0.066 | 0.122 | ok |

## Against r3: Video by kurzgesagt

| axis | measure | ours | reference | verdict |
| --- | --- | --- | --- | --- |
| pace | visual beats per 10 s | 4.97 | 3.17 | near |
| pace | gap between beats, median s | 1.8 | 2.3 | ok |
| pace | shot length, median s | 1.9 | 2.3 | ok |
| pace | hard-cut share of shot changes | 0.94 | 0.48 | near |
| ground | background hold, median s | 1.9 | 1.8 | ok |
| ground | plain ground share of frame | 0.668 | 0.174 | off |
| motion | motion, median | 0.0098 | 0.0251 | near |
| motion | motion, p90 | 0.0375 | 0.0795 | near |
| motion | static share of time | 0.066 | 0.157 | ok |

## Sound (fixed targets, not the reference)

| axis | measure | ours | target | verdict |
| --- | --- | --- | --- | --- |
| sound | loudness, LUFS | -13.0 | -16 to -14 | near |
| sound | true peak, dBTP | -1.4 | -1 or lower | ok |

Skipped axes: colour, palette. Palette swatches: `/Users/rajdeepmalladeb/Downloads/claude not free/atomz-trend-reel/qa/swatches.png`.

These numbers flag drift; they do not prove a match. `off` on an axis the style takes from the reference is a fix; `near` is a judgement. Look at `contact.jpg`, `hook.jpg` and `events.jpg` beside the reference's.
