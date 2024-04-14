from _typeshed import Incomplete

class TextFitter(tuple):
    def __new__(cls, line_source, extents, font_file): ...
    @classmethod
    def best_fit_font_size(cls, text, extents, max_size, font_file): ...

class _BinarySearchTree:
    def __init__(self, value) -> None: ...
    def find_max(self, predicate, max_: Incomplete | None = None): ...
    @classmethod
    def from_ordered_sequence(cls, iseq): ...
    def insert(self, value) -> None: ...
    def tree(self, level: int = 0, prefix: str = ''): ...
    @property
    def value(self): ...

class _LineSource:
    def __init__(self, text) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other): ...
    def __iter__(self): ...
    def __nonzero__(self): ...

class _Line(tuple):
    def __new__(cls, text, remainder): ...
    def __gt__(self, other): ...
    def __lt__(self, other): ...
    def __len__(self) -> int: ...
    @property
    def remainder(self): ...
    @property
    def text(self): ...

class _Fonts:
    fonts: Incomplete
    @classmethod
    def font(cls, font_path, point_size): ...
