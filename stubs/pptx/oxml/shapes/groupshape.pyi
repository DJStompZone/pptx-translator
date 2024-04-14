from _typeshed import Incomplete
from collections.abc import Generator
from pptx.enum.shapes import MSO_CONNECTOR_TYPE as MSO_CONNECTOR_TYPE
from pptx.oxml import parse_xml as parse_xml
from pptx.oxml.ns import nsdecls as nsdecls, qn as qn
from pptx.oxml.shapes.autoshape import CT_Shape as CT_Shape
from pptx.oxml.shapes.connector import CT_Connector as CT_Connector
from pptx.oxml.shapes.graphfrm import CT_GraphicalObjectFrame as CT_GraphicalObjectFrame
from pptx.oxml.shapes.picture import CT_Picture as CT_Picture
from pptx.oxml.shapes.shared import BaseShapeElement as BaseShapeElement
from pptx.oxml.xmlchemy import BaseOxmlElement as BaseOxmlElement, OneAndOnlyOne as OneAndOnlyOne, ZeroOrOne as ZeroOrOne
from pptx.util import Emu as Emu

class CT_GroupShape(BaseShapeElement):
    nvGrpSpPr: Incomplete
    grpSpPr: Incomplete
    def add_autoshape(self, id_, name, prst, x, y, cx, cy): ...
    def add_cxnSp(self, id_, name, type_member, x, y, cx, cy, flipH, flipV): ...
    def add_freeform_sp(self, x, y, cx, cy): ...
    def add_grpSp(self): ...
    def add_pic(self, id_, name, desc, rId, x, y, cx, cy): ...
    def add_placeholder(self, id_, name, ph_type, orient, sz, idx): ...
    def add_table(self, id_, name, rows, cols, x, y, cx, cy): ...
    def add_textbox(self, id_, name, x, y, cx, cy): ...
    @property
    def chExt(self): ...
    @property
    def chOff(self): ...
    def get_or_add_xfrm(self): ...
    def iter_ph_elms(self) -> Generator[Incomplete, None, None]: ...
    def iter_shape_elms(self) -> Generator[Incomplete, None, None]: ...
    @property
    def max_shape_id(self): ...
    @classmethod
    def new_grpSp(cls, id_, name): ...
    def recalculate_extents(self) -> None: ...
    @property
    def xfrm(self): ...

class CT_GroupShapeNonVisual(BaseShapeElement):
    cNvPr: Incomplete

class CT_GroupShapeProperties(BaseOxmlElement):
    xfrm: Incomplete
    effectLst: Incomplete
