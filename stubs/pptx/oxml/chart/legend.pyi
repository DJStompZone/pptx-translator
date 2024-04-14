from ...enum.chart import XL_LEGEND_POSITION as XL_LEGEND_POSITION
from ..text import CT_TextBody as CT_TextBody
from ..xmlchemy import BaseOxmlElement as BaseOxmlElement, OptionalAttribute as OptionalAttribute, ZeroOrOne as ZeroOrOne
from _typeshed import Incomplete

class CT_Legend(BaseOxmlElement):
    legendPos: Incomplete
    layout: Incomplete
    overlay: Incomplete
    txPr: Incomplete
    @property
    def defRPr(self): ...
    @property
    def horz_offset(self): ...
    @horz_offset.setter
    def horz_offset(self, offset) -> None: ...

class CT_LegendPos(BaseOxmlElement):
    val: Incomplete
