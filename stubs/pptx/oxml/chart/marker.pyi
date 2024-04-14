from ...enum.chart import XL_MARKER_STYLE as XL_MARKER_STYLE
from ..simpletypes import ST_MarkerSize as ST_MarkerSize
from ..xmlchemy import BaseOxmlElement as BaseOxmlElement, RequiredAttribute as RequiredAttribute, ZeroOrOne as ZeroOrOne
from _typeshed import Incomplete

class CT_Marker(BaseOxmlElement):
    symbol: Incomplete
    size: Incomplete
    spPr: Incomplete
    @property
    def size_val(self): ...
    @property
    def symbol_val(self): ...

class CT_MarkerSize(BaseOxmlElement):
    val: Incomplete

class CT_MarkerStyle(BaseOxmlElement):
    val: Incomplete
