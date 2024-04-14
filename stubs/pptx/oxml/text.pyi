from _typeshed import Incomplete
from pptx.compat import to_unicode as to_unicode
from pptx.enum.lang import MSO_LANGUAGE_ID as MSO_LANGUAGE_ID
from pptx.enum.text import MSO_AUTO_SIZE as MSO_AUTO_SIZE, MSO_TEXT_UNDERLINE_TYPE as MSO_TEXT_UNDERLINE_TYPE, MSO_VERTICAL_ANCHOR as MSO_VERTICAL_ANCHOR, PP_PARAGRAPH_ALIGNMENT as PP_PARAGRAPH_ALIGNMENT
from pptx.exc import InvalidXmlError as InvalidXmlError
from pptx.oxml import parse_xml as parse_xml
from pptx.oxml.dml.fill import CT_GradientFillProperties as CT_GradientFillProperties
from pptx.oxml.ns import nsdecls as nsdecls
from pptx.oxml.simpletypes import ST_Coordinate32 as ST_Coordinate32, ST_TextFontScalePercentOrPercentString as ST_TextFontScalePercentOrPercentString, ST_TextFontSize as ST_TextFontSize, ST_TextIndentLevelType as ST_TextIndentLevelType, ST_TextSpacingPercentOrPercentString as ST_TextSpacingPercentOrPercentString, ST_TextSpacingPoint as ST_TextSpacingPoint, ST_TextTypeface as ST_TextTypeface, ST_TextWrappingType as ST_TextWrappingType, XsdBoolean as XsdBoolean
from pptx.oxml.xmlchemy import BaseOxmlElement as BaseOxmlElement, Choice as Choice, OneAndOnlyOne as OneAndOnlyOne, OneOrMore as OneOrMore, OptionalAttribute as OptionalAttribute, RequiredAttribute as RequiredAttribute, ZeroOrMore as ZeroOrMore, ZeroOrOne as ZeroOrOne, ZeroOrOneChoice as ZeroOrOneChoice
from pptx.util import Emu as Emu, Length as Length

class CT_RegularTextRun(BaseOxmlElement):
    rPr: Incomplete
    t: Incomplete
    @property
    def text(self): ...
    @text.setter
    def text(self, str) -> None: ...

class CT_TextBody(BaseOxmlElement):
    bodyPr: Incomplete
    p: Incomplete
    def clear_content(self) -> None: ...
    @property
    def defRPr(self): ...
    @property
    def is_empty(self): ...
    @classmethod
    def new(cls): ...
    @classmethod
    def new_a_txBody(cls): ...
    @classmethod
    def new_p_txBody(cls): ...
    @classmethod
    def new_txPr(cls): ...
    def unclear_content(self) -> None: ...

class CT_TextBodyProperties(BaseOxmlElement):
    eg_textAutoFit: Incomplete
    lIns: Incomplete
    tIns: Incomplete
    rIns: Incomplete
    bIns: Incomplete
    anchor: Incomplete
    wrap: Incomplete
    @property
    def autofit(self): ...
    @autofit.setter
    def autofit(self, value) -> None: ...

class CT_TextCharacterProperties(BaseOxmlElement):
    eg_fillProperties: Incomplete
    latin: Incomplete
    hlinkClick: Incomplete
    lang: Incomplete
    sz: Incomplete
    b: Incomplete
    i: Incomplete
    u: Incomplete
    def add_hlinkClick(self, rId): ...

class CT_TextField(BaseOxmlElement):
    rPr: Incomplete
    t: Incomplete
    @property
    def text(self): ...

class CT_TextFont(BaseOxmlElement):
    typeface: Incomplete

class CT_TextLineBreak(BaseOxmlElement):
    rPr: Incomplete
    @property
    def text(self): ...

class CT_TextNormalAutofit(BaseOxmlElement):
    fontScale: Incomplete

class CT_TextParagraph(BaseOxmlElement):
    pPr: Incomplete
    r: Incomplete
    br: Incomplete
    endParaRPr: Incomplete
    def add_br(self): ...
    def add_r(self, text: Incomplete | None = None): ...
    def append_text(self, text) -> None: ...
    @property
    def content_children(self): ...
    @property
    def text(self): ...

class CT_TextParagraphProperties(BaseOxmlElement):
    lnSpc: Incomplete
    spcBef: Incomplete
    spcAft: Incomplete
    defRPr: Incomplete
    lvl: Incomplete
    algn: Incomplete
    @property
    def line_spacing(self): ...
    @line_spacing.setter
    def line_spacing(self, value) -> None: ...
    @property
    def space_after(self): ...
    @space_after.setter
    def space_after(self, value) -> None: ...
    @property
    def space_before(self): ...
    @space_before.setter
    def space_before(self, value) -> None: ...

class CT_TextSpacing(BaseOxmlElement):
    spcPct: Incomplete
    spcPts: Incomplete
    def set_spcPct(self, value) -> None: ...
    def set_spcPts(self, value) -> None: ...

class CT_TextSpacingPercent(BaseOxmlElement):
    val: Incomplete

class CT_TextSpacingPoint(BaseOxmlElement):
    val: Incomplete
