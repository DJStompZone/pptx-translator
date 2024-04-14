from .simpletypes import ST_SlideId as ST_SlideId, ST_SlideSizeCoordinate as ST_SlideSizeCoordinate, XsdString as XsdString
from .xmlchemy import BaseOxmlElement as BaseOxmlElement, RequiredAttribute as RequiredAttribute, ZeroOrMore as ZeroOrMore, ZeroOrOne as ZeroOrOne
from _typeshed import Incomplete

class CT_Presentation(BaseOxmlElement):
    sldMasterIdLst: Incomplete
    sldIdLst: Incomplete
    sldSz: Incomplete

class CT_SlideId(BaseOxmlElement):
    id: Incomplete
    rId: Incomplete

class CT_SlideIdList(BaseOxmlElement):
    sldId: Incomplete
    def add_sldId(self, rId): ...

class CT_SlideMasterIdList(BaseOxmlElement):
    sldMasterId: Incomplete

class CT_SlideMasterIdListEntry(BaseOxmlElement):
    rId: Incomplete

class CT_SlideSize(BaseOxmlElement):
    cx: Incomplete
    cy: Incomplete
