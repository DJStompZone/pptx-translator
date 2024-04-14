from .. import parse_xml as parse_xml
from ..ns import nsdecls as nsdecls
from ..simpletypes import ST_DrawingElementId as ST_DrawingElementId, XsdUnsignedInt as XsdUnsignedInt
from ..xmlchemy import BaseOxmlElement as BaseOxmlElement, OneAndOnlyOne as OneAndOnlyOne, RequiredAttribute as RequiredAttribute, ZeroOrOne as ZeroOrOne
from .shared import BaseShapeElement as BaseShapeElement
from _typeshed import Incomplete

class CT_Connection(BaseShapeElement):
    id: Incomplete
    idx: Incomplete

class CT_Connector(BaseShapeElement):
    nvCxnSpPr: Incomplete
    spPr: Incomplete
    @classmethod
    def new_cxnSp(cls, id_, name, prst, x, y, cx, cy, flipH, flipV): ...

class CT_ConnectorNonVisual(BaseOxmlElement):
    cNvPr: Incomplete
    cNvCxnSpPr: Incomplete
    nvPr: Incomplete

class CT_NonVisualConnectorProperties(BaseOxmlElement):
    stCxn: Incomplete
    endCxn: Incomplete
