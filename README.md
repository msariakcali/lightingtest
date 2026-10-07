# turkce-tts

[EMA Lightning](https://huggingface.co/canberkkkkkk/ema-lightning) modeliyle Türkçe metinden konuşma (TTS) testi.
Metni yazıp Enter'a basınca ses üretilir, `out/` klasörüne WAV olarak kaydedilir ve çalınır.

## Gereksinimler

- Python **3.11 veya üstü**
- Linux'ta `libsndfile`: `sudo apt install libsndfile1`
- Linux'ta ses çalmak için `pw-play`, `paplay`, `aplay` veya `ffplay` komutlarından biri (yoksa ses sadece dosyaya kaydedilir)

## Kurulum

```bash
git clone https://github.com/msariakcali/lightingtest.git
cd lightingtest
```

Sanal ortamı oluştur ve etkinleştir:

```bash
# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate
```

Paketleri kur:

```bash
pip install -r requirements.txt
```

> **Not:** Linux'ta `torch` varsayılan olarak GPU (CUDA) sürümüyle kurulur ve birkaç GB tutar.
> Sadece CPU kullanacaksan, `requirements.txt`'den **önce** şunu çalıştır:
>
> ```bash
> pip install torch --index-url https://download.pytorch.org/whl/cpu
> ```

## Kullanım

```bash
python test_tts.py
```

```
Metin> Merhaba, size nasıl yardımcı olabilirim?
  2.00 sn ses, 412 ms'de üretildi -> cikti_001.wav
Metin>
```

Çıkmak için boş satır, `q` veya `Ctrl+C`.

## Model

Model ağırlıkları (~34 MB) ilk çalıştırmada Hugging Face'ten otomatik iner ve
`~/.cache/huggingface/hub` altına önbelleğe alınır; sonraki çalıştırmalarda tekrar inmez.

- 48 kHz, tek konuşmacı, mono
- İlk üretim yavaş olabilir (ısınma); sonrakiler çok daha hızlıdır
- Lisans: Apache 2.0
