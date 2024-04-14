from _typeshed import Incomplete
from pptx.enum.dml import MSO_PATTERN_TYPE as MSO_PATTERN_TYPE
from pptx.oxml import parse_xml as parse_xml
from pptx.oxml.ns import nsdecls as nsdecls
from pptx.oxml.simpletypes import ST_Percentage as ST_Percentage, ST_PositiveFixedAngle as ST_PositiveFixedAngle, ST_PositiveFixedPercentage as ST_PositiveFixedPercentage, ST_RelationshipId as ST_RelationshipId
from pptx.oxml.xmlchemy import BaseOxmlElement as BaseOxmlElement, Choice as Choice, OneOrMore as OneOrMore, OptionalAttribute as OptionalAttribute, RequiredAttribute as RequiredAttribute, ZeroOrOne as ZeroOrOne, ZeroOrOneChoice as ZeroOrOneChoice

class CT_Blip(BaseOxmlElement):
    rEmbed: Incomplete

class CT_BlipFillProperties(BaseOxmlElement):
    blip: Incomplete
    srcRect: Incomplete
    def crop(self, cropping) -> None: ...

class CT_GradientFillProperties(BaseOxmlElement):
    gsLst: Incomplete
    lin: Incomplete
    path: Incomplete
    @classmethod
    def new_gradFill(cls): ...

class CT_GradientStop(BaseOxmlElement):
    eg_colorChoice: Incomplete
    pos: Incomplete

class CT_GradientStopList(BaseOxmlElement):
    gs: Incomplete
    @classmethod
    def new_gsLst(cls): ...

class CT_GroupFillProperties(BaseOxmlElement): ...

class CT_LinearShadeProperties(BaseOxmlElement):
    ang: Incomplete

class CT_NoFillProperties(BaseOxmlElement): ...

class CT_PatternFillProperties(BaseOxmlElement):
    fgClr: Incomplete
    bgClr: Incomplete
    prst: Incomplete

class CT_RelativeRect(BaseOxmlElement):
    l: Incomplete
    t: Incomplete
    r: Incomplete
    b: Incomplete

class CT_SolidColorFillProperties(BaseOxmlElement):
    eg_colorChoice: Incomplete
