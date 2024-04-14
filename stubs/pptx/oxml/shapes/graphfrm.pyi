from _typeshed import Incomplete
from pptx.oxml import parse_xml as parse_xml
from pptx.oxml.chart.chart import CT_Chart as CT_Chart
from pptx.oxml.ns import nsdecls as nsdecls
from pptx.oxml.shapes.shared import BaseShapeElement as BaseShapeElement
from pptx.oxml.simpletypes import XsdBoolean as XsdBoolean, XsdString as XsdString
from pptx.oxml.table import CT_Table as CT_Table
from pptx.oxml.xmlchemy import BaseOxmlElement as BaseOxmlElement, OneAndOnlyOne as OneAndOnlyOne, OptionalAttribute as OptionalAttribute, RequiredAttribute as RequiredAttribute, ZeroOrOne as ZeroOrOne
from pptx.spec import GRAPHIC_DATA_URI_CHART as GRAPHIC_DATA_URI_CHART, GRAPHIC_DATA_URI_OLEOBJ as GRAPHIC_DATA_URI_OLEOBJ, GRAPHIC_DATA_URI_TABLE as GRAPHIC_DATA_URI_TABLE

class CT_GraphicalObject(BaseOxmlElement):
    graphicData: Incomplete
    @property
    def chart(self): ...

class CT_GraphicalObjectData(BaseShapeElement):
    chart: Incomplete
    tbl: Incomplete
    uri: Incomplete
    @property
    def blob_rId(self): ...
    @property
    def is_embedded_ole_obj(self): ...
    @property
    def progId(self): ...
    @property
    def showAsIcon(self): ...

class CT_GraphicalObjectFrame(BaseShapeElement):
    nvGraphicFramePr: Incomplete
    xfrm: Incomplete
    graphic: Incomplete
    @property
    def chart(self): ...
    @property
    def chart_rId(self): ...
    def get_or_add_xfrm(self): ...
    @property
    def graphicData(self): ...
    @property
    def graphicData_uri(self): ...
    @property
    def has_oleobj(self): ...
    @property
    def is_embedded_ole_obj(self): ...
    @classmethod
    def new_chart_graphicFrame(cls, id_, name, rId, x, y, cx, cy): ...
    @classmethod
    def new_graphicFrame(cls, id_, name, x, y, cx, cy): ...
    @classmethod
    def new_ole_object_graphicFrame(cls, id_, name, ole_object_rId, progId, icon_rId, x, y, cx, cy, imgW, imgH): ...
    @classmethod
    def new_table_graphicFrame(cls, id_, name, rows, cols, x, y, cx, cy): ...

class CT_GraphicalObjectFrameNonVisual(BaseOxmlElement):
    cNvPr: Incomplete
    nvPr: Incomplete

class CT_OleObject(BaseOxmlElement):
    progId: Incomplete
    rId: Incomplete
    showAsIcon: Incomplete
    @property
    def is_embedded(self): ...
