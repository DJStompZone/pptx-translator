from _typeshed import Incomplete
from pptx.compat import Sequence as Sequence

class Categories(Sequence):
    def __init__(self, xChart) -> None: ...
    def __getitem__(self, idx): ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    @property
    def depth(self): ...
    @property
    def flattened_labels(self): ...
    @property
    def levels(self): ...

class Category(str):
    def __new__(cls, pt, *args): ...
    def __init__(self, pt, idx: Incomplete | None = None) -> None: ...
    @property
    def idx(self): ...
    @property
    def label(self): ...

class CategoryLevel(Sequence):
    def __init__(self, lvl) -> None: ...
    def __getitem__(self, offset): ...
    def __len__(self) -> int: ...
