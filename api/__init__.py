import sys
from pathlib import Path

# Jika scipy asli tidak terpasang (dibuang demi ukuran bundle Vercel), pakai stub minimal.
try:
    import scipy.sparse  # noqa: F401
except ImportError:
    sys.path.insert(0, str(Path(__file__).resolve().parent / "_stubs"))
