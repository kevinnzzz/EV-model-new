---
title: EV Model API
emoji: 🚗
colorFrom: green
colorTo: blue
sdk: docker
app_port: 7860
pinned: false
---

# EV Model API

API FastAPI untuk prediksi ketertarikan EV. Dokumentasi: `/docs`.

## Deploy ke Vercel (bundle < 500 MB)

- Dependency dibatasi di `pyproject.toml` (+ `uv.lock`); `scipy`, `plotly`, `matplotlib`, `graphviz` dibuang.
- `api/_stubs/scipy` adalah stub kecil pengganti scipy (CatBoost hanya perlu `scipy.sparse` untuk isinstance).
- `model/cat.cbm.gz` didekompres otomatis ke `/tmp` saat start (lihat `api/config.py`).
- **Wajib:** folder/paket `ev_web` (dipakai `api/predictor.py`) harus ikut disertakan di repo.
- Untuk Render/Hugging Face/lokal pakai `requirements-full.txt`.
