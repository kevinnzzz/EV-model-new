"""Stub scipy.sparse: kelas-kelas sparse hanya dipakai CatBoost untuk isinstance(),
dan API ini tidak pernah mengirim data sparse."""


class spmatrix:  # noqa: N801
    pass


def issparse(_x):
    return False


def __getattr__(name):
    # csr_matrix, csc_matrix, coo_matrix, dia_matrix, ... -> kelas kosong (tidak pernah cocok)
    if name.startswith("__"):
        raise AttributeError(name)
    cls = type(name, (spmatrix,), {})
    globals()[name] = cls
    return cls
