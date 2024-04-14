from _typeshed import Incomplete
from pptx.dml.fill import CT_GradientFillProperties as CT_GradientFillProperties
from pptx.enum.shapes import PP_PLACEHOLDER as PP_PLACEHOLDER
from pptx.oxml.ns import qn as qn
from pptx.oxml.simpletypes import ST_Angle as ST_Angle, ST_Coordinate as ST_Coordinate, ST_Direction as ST_Direction, ST_DrawingElementId as ST_DrawingElementId, ST_LineWidth as ST_LineWidth, ST_PlaceholderSize as ST_PlaceholderSize, ST_PositiveCoordinate as ST_PositiveCoordinate, XsdBoolean as XsdBoolean, XsdString as XsdString, XsdUnsignedInt as XsdUnsignedInt
from pptx.oxml.xmlchemy import BaseOxmlElement as BaseOxmlElement, Choice as Choice, OptionalAttribute as OptionalAttribute, OxmlElement as OxmlElement, RequiredAttribute as RequiredAttribute, ZeroOrOne as ZeroOrOne, ZeroOrOneChoice as ZeroOrOneChoice
from pptx.util import Emu as Emu

class BaseShapeElement(BaseOxmlElement):
    @property
    def cx(self): ...
    @cx.setter
    def cx(self, value) -> None: ...
    @property
    def cy(self): ...
    @cy.setter
    def cy(self, value) -> None: ...
    @property
    def flipH(self): ...
    @flipH.setter
    def flipH(self, value) -> None: ...
    @property
    def flipV(self): ...
    @flipV.setter
    def flipV(self, value) -> None: ...
    def get_or_add_xfrm(self): ...
    @property
    def has_ph_elm(self): ...
    @property
    def ph(self): ...
    @property
    def ph_idx(self): ...
    @property
    def ph_orient(self): ...
    @property
    def ph_sz(self): ...
    @property
    def ph_type(self): ...
    @property
    def rot(self): ...
    @rot.setter
    def rot(self, value) -> None: ...
    @property
    def shape_id(self): ...
    @property
    def shape_name(self): ...
    @property
    def txBody(self): ...
    @property
    def x(self): ...
    @x.setter
    def x(self, value) -> None: ...
    @property
    def xfrm(self): ...
    @property
    def y(self): ...
    @y.setter
    def y(self, value) -> None: ...

class CT_ApplicationNonVisualDrawingProps(BaseOxmlElement):
    ph: Incomplete

class CT_LineProperties(BaseOxmlElement):
    eg_lineFillProperties: Incomplete
    prstDash: Incomplete
    custDash: Incomplete
    w: Incomplete
    @property
    def eg_fillProperties(self): ...
    @property
    def prstDash_val(self): ...
    @prstDash_val.setter
    def prstDash_val(self, val) -> None: ...

class CT_NonVisualDrawingProps(BaseOxmlElement):
    hlinkClick: Incomplete
    hlinkHover: Incomplete
    id: Incomplete
    name: Incomplete

class CT_Placeholder(BaseOxmlElement):
    type: Incomplete
    orient: Incomplete
    sz: Incomplete
    idx: Incomplete

class CT_Point2D(BaseOxmlElement):
    x: Incomplete
    y: Incomplete

class CT_PositiveSize2D(BaseOxmlElement):
    cx: Incomplete
    cy: Incomplete

class CT_ShapeProperties(BaseOxmlElement):
    xfrm: Incomplete
    custGeom: Incomplete
    prstGeom: Incomplete
    eg_fillProperties: Incomplete
    ln: Incomplete
    effectLst: Incomplete
    @property
    def cx(self): ...
    @property
    def cy(self): ...
    @property
    def x(self): ...
    @property
    def y(self): ...

class CT_Transform2D(BaseOxmlElement):
    off: Incomplete
    ext: Incomplete
    chOff: Incomplete
    chExt: Incomplete
    rot: Incomplete
    flipH: Incomplete
    flipV: Incomplete
    @property
    def x(self): ...
    @x.setter
    def x(self, value) -> None: ...
    @property
    def y(self): ...
    @y.setter
    def y(self, value) -> None: ...
    @property
    def cx(self): ...
    @cx.setter
    def cx(self, value) -> None: ...
    @property
    def cy(self): ...
    @cy.setter
    def cy(self, value) -> None: ...
