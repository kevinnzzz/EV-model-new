import os
from pathlib import Path

import gzip
import shutil
import tempfile

BASE_DIR = Path(__file__).resolve().parent.parent
_SRC_MODEL_DIR = BASE_DIR / "model"


def _prepare_model_dir() -> Path:
    """cat.cbm disimpan dalam bentuk .gz (91 MB -> 29 MB) agar bundle Vercel < 500 MB.
    Saat start, file di-decompress ke folder sementara (/tmp) lalu dipakai dari sana."""
    gz = _SRC_MODEL_DIR / "cat.cbm.gz"
    if not gz.exists():
        return _SRC_MODEL_DIR  # model tidak dikompres (mis. jalan lokal)

    target = Path(tempfile.gettempdir()) / "ev_model"
    target.mkdir(parents=True, exist_ok=True)
    for f in _SRC_MODEL_DIR.iterdir():
        if f.is_file() and f.suffix != ".gz" and not (target / f.name).exists():
            shutil.copy2(f, target / f.name)
    out = target / "cat.cbm"
    if not out.exists():  # instance yang masih hangat tidak perlu decompress ulang
        tmp = target / "cat.cbm.part"
        with gzip.open(gz, "rb") as src, open(tmp, "wb") as dst:
            shutil.copyfileobj(src, dst)
        tmp.replace(out)
    return target


MODEL_DIR = _prepare_model_dir()

# Alamat website yang boleh memanggil API ini, pisahkan dengan koma.
# Mencakup semua port localhost umum (5173, 5174, 5175, 3000) dan domain hosting
ALLOWED_ORIGINS = [
    o.strip()
    for o in os.getenv(
        "ALLOWED_ORIGINS",
        "http://localhost:5173,http://127.0.0.1:5173,http://localhost:5174,http://127.0.0.1:5174,http://localhost:5175,http://127.0.0.1:5175,http://localhost:3000,http://127.0.0.1:3000",
    ).split(",")
    if o.strip()
]