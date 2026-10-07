import os
import sys
import time

os.environ.setdefault("HF_HUB_DISABLE_SYMLINKS_WARNING", "1")

import winsound
from pathlib import Path

import soundfile as sf

from ema_lightning import EMA

OUT_DIR = Path(__file__).parent / "out"
OUT_DIR.mkdir(exist_ok=True)


def main() -> None:
    print("Model yükleniyor (ilk çalıştırmada Hugging Face'ten ~34 MB iner)...")
    t0 = time.perf_counter()
    tts = EMA()
    print(f"Hazır ({time.perf_counter() - t0:.1f} sn). Metin gir, Enter'a bas. Çıkış: boş satır / q\n")

    n = 0
    while True:
        try:
            text = input("Metin> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not text or text.lower() in {"q", "quit", "exit"}:
            break

        t0 = time.perf_counter()
        speech = tts.say(text)
        gen = time.perf_counter() - t0

        n += 1
        path = OUT_DIR / f"cikti_{n:03d}.wav"
        sf.write(path, speech.audio, speech.sample_rate)
        print(f"  {speech.duration:.2f} sn ses, {gen * 1000:.0f} ms'de üretildi -> {path.name}")

        winsound.PlaySound(str(path), winsound.SND_FILENAME)


if __name__ == "__main__":
    sys.exit(main())
