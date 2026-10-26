"""Stub minimal pengganti scipy (hanya dipakai jika scipy asli tidak terpasang).

CatBoost hanya melakukan `import scipy.sparse` dan isinstance(data, scipy.sparse.spmatrix)
untuk mendukung input sparse. API ini tidak pernah mengirim data sparse,
jadi stub ini cukup dan menghemat ~115 MB.
"""
