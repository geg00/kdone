# AUTOGENERATED! DO NOT EDIT! File to edit: ../03_document.ipynb.

# %% auto 0
__all__ = ['Document']

# %% ../03_document.ipynb 3
class Document:
    "A Document of Pages"
    def __init__(self): 
        self.pages = []
    def __str__(self): return [page for page in self.pages]
