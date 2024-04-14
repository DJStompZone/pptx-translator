from _typeshed import Incomplete
from pptx.dml.fill import FillFormat as FillFormat
from pptx.dml.line import LineFormat as LineFormat
from pptx.enum.shapes import MSO_AUTO_SHAPE_TYPE as MSO_AUTO_SHAPE_TYPE, MSO_SHAPE_TYPE as MSO_SHAPE_TYPE
from pptx.shapes.base import BaseShape as BaseShape
from pptx.spec import autoshape_types as autoshape_types
from pptx.text.text import TextFrame as TextFrame
from pptx.util import lazyproperty as lazyproperty

class Adjustment:
    name: Incomplete
    def_val: Incomplete
    actual: Incomplete
    def __init__(self, name, def_val, actual: Incomplete | None = None) -> None: ...
    @property
    def effective_value(self): ...
    @effective_value.setter
    def effective_value(self, value) -> None: ...
    @property
    def val(self): ...

class AdjustmentCollection:
    def __init__(self, prstGeom) -> None: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def __len__(self) -> int: ...

class AutoShapeType:
    def __new__(cls, autoshape_type_id): ...
    def __init__(self, autoshape_type_id) -> None: ...
    @property
    def autoshape_type_id(self): ...
    @property
    def basename(self): ...
    @classmethod
    def default_adjustment_values(cls, prst): ...
    @property
    def desc(self): ...
    @classmethod
    def id_from_prst(cls, prst): ...
    @property
    def prst(self): ...

class Shape(BaseShape):
    def __init__(self, sp, parent) -> None: ...
    def adjustments(self): ...
    @property
    def auto_shape_type(self): ...
    def fill(self): ...
    def get_or_add_ln(self): ...
    @property
    def has_text_frame(self): ...
    def line(self): ...
    @property
    def ln(self): ...
    @property
    def shape_type(self): ...
    @property
    def text(self): ...
    @text.setter
    def text(self, text) -> None: ...
    @property
    def text_frame(self): ...