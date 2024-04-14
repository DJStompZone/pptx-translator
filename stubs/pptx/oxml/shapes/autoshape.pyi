from _typeshed import Incomplete
from pptx.enum.shapes import MSO_AUTO_SHAPE_TYPE as MSO_AUTO_SHAPE_TYPE, PP_PLACEHOLDER as PP_PLACEHOLDER
from pptx.oxml import parse_xml as parse_xml
from pptx.oxml.ns import nsdecls as nsdecls
from pptx.oxml.shapes.shared import BaseShapeElement as BaseShapeElement
from pptx.oxml.simpletypes import ST_Coordinate as ST_Coordinate, ST_PositiveCoordinate as ST_PositiveCoordinate, XsdBoolean as XsdBoolean, XsdString as XsdString
from pptx.oxml.text import CT_TextBody as CT_TextBody
from pptx.oxml.xmlchemy import BaseOxmlElement as BaseOxmlElement, OneAndOnlyOne as OneAndOnlyOne, OptionalAttribute as OptionalAttribute, RequiredAttribute as RequiredAttribute, ZeroOrMore as ZeroOrMore, ZeroOrOne as ZeroOrOne

class CT_AdjPoint2D(BaseOxmlElement):
    x: Incomplete
    y: Incomplete

class CT_CustomGeometry2D(BaseOxmlElement):
    pathLst: Incomplete

class CT_GeomGuide(BaseOxmlElement):
    name: Incomplete
    fmla: Incomplete

class CT_GeomGuideList(BaseOxmlElement):
    gd: Incomplete

class CT_NonVisualDrawingShapeProps(BaseShapeElement):
    spLocks: Incomplete
    txBox: Incomplete

class CT_Path2D(BaseOxmlElement):
    close: Incomplete
    lnTo: Incomplete
    moveTo: Incomplete
    w: Incomplete
    h: Incomplete
    def add_close(self): ...
    def add_lnTo(self, x, y): ...
    def add_moveTo(self, x, y): ...

class CT_Path2DClose(BaseOxmlElement): ...

class CT_Path2DLineTo(BaseOxmlElement):
    pt: Incomplete

class CT_Path2DList(BaseOxmlElement):
    path: Incomplete
    def add_path(self, w, h): ...

class CT_Path2DMoveTo(BaseOxmlElement):
    pt: Incomplete

class CT_PresetGeometry2D(BaseOxmlElement):
    avLst: Incomplete
    prst: Incomplete
    @property
    def gd_lst(self): ...
    def rewrite_guides(self, guides) -> None: ...

class CT_Shape(BaseShapeElement):
    nvSpPr: Incomplete
    spPr: Incomplete
    txBody: Incomplete
    def add_path(self, w, h): ...
    def get_or_add_ln(self): ...
    @property
    def has_custom_geometry(self): ...
    @property
    def is_autoshape(self): ...
    @property
    def is_textbox(self): ...
    @property
    def ln(self): ...
    @staticmethod
    def new_autoshape_sp(id_, name, prst, left, top, width, height): ...
    @staticmethod
    def new_freeform_sp(shape_id, name, x, y, cx, cy): ...
    @staticmethod
    def new_placeholder_sp(id_, name, ph_type, orient, sz, idx): ...
    @staticmethod
    def new_textbox_sp(id_, name, left, top, width, height): ...
    @property
    def prst(self): ...
    @property
    def prstGeom(self): ...

class CT_ShapeNonVisual(BaseShapeElement):
    cNvPr: Incomplete
    cNvSpPr: Incomplete
    nvPr: Incomplete
