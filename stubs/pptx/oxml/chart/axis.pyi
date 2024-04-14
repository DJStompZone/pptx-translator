from _typeshed import Incomplete
from pptx.enum.chart import XL_AXIS_CROSSES as XL_AXIS_CROSSES, XL_TICK_LABEL_POSITION as XL_TICK_LABEL_POSITION, XL_TICK_MARK as XL_TICK_MARK
from pptx.oxml.chart.shared import CT_Title as CT_Title
from pptx.oxml.simpletypes import ST_AxisUnit as ST_AxisUnit, ST_LblOffset as ST_LblOffset, ST_Orientation as ST_Orientation
from pptx.oxml.text import CT_TextBody as CT_TextBody
from pptx.oxml.xmlchemy import BaseOxmlElement as BaseOxmlElement, OneAndOnlyOne as OneAndOnlyOne, OptionalAttribute as OptionalAttribute, RequiredAttribute as RequiredAttribute, ZeroOrOne as ZeroOrOne

class BaseAxisElement(BaseOxmlElement):
    @property
    def defRPr(self): ...
    @property
    def orientation(self): ...
    @orientation.setter
    def orientation(self, value) -> None: ...

class CT_AxisUnit(BaseOxmlElement):
    val: Incomplete

class CT_CatAx(BaseAxisElement):
    scaling: Incomplete
    delete_: Incomplete
    majorGridlines: Incomplete
    minorGridlines: Incomplete
    title: Incomplete
    numFmt: Incomplete
    majorTickMark: Incomplete
    minorTickMark: Incomplete
    tickLblPos: Incomplete
    spPr: Incomplete
    txPr: Incomplete
    crosses: Incomplete
    crossesAt: Incomplete
    lblOffset: Incomplete

class CT_ChartLines(BaseOxmlElement):
    spPr: Incomplete

class CT_Crosses(BaseOxmlElement):
    val: Incomplete

class CT_DateAx(BaseAxisElement):
    scaling: Incomplete
    delete_: Incomplete
    majorGridlines: Incomplete
    minorGridlines: Incomplete
    title: Incomplete
    numFmt: Incomplete
    majorTickMark: Incomplete
    minorTickMark: Incomplete
    tickLblPos: Incomplete
    spPr: Incomplete
    txPr: Incomplete
    crosses: Incomplete
    crossesAt: Incomplete
    lblOffset: Incomplete

class CT_LblOffset(BaseOxmlElement):
    val: Incomplete

class CT_Orientation(BaseOxmlElement):
    val: Incomplete

class CT_Scaling(BaseOxmlElement):
    orientation: Incomplete
    max: Incomplete
    min: Incomplete
    @property
    def maximum(self): ...
    @maximum.setter
    def maximum(self, value) -> None: ...
    @property
    def minimum(self): ...
    @minimum.setter
    def minimum(self, value) -> None: ...

class CT_TickLblPos(BaseOxmlElement):
    val: Incomplete

class CT_TickMark(BaseOxmlElement):
    val: Incomplete

class CT_ValAx(BaseAxisElement):
    scaling: Incomplete
    delete_: Incomplete
    majorGridlines: Incomplete
    minorGridlines: Incomplete
    title: Incomplete
    numFmt: Incomplete
    majorTickMark: Incomplete
    minorTickMark: Incomplete
    tickLblPos: Incomplete
    spPr: Incomplete
    txPr: Incomplete
    crossAx: Incomplete
    crosses: Incomplete
    crossesAt: Incomplete
    majorUnit: Incomplete
    minorUnit: Incomplete
