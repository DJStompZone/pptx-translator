from _typeshed import Incomplete
from pptx.oxml import parse_from_template as parse_from_template, parse_xml as parse_xml
from pptx.oxml.dml.fill import CT_GradientFillProperties as CT_GradientFillProperties
from pptx.oxml.ns import nsdecls as nsdecls
from pptx.oxml.simpletypes import XsdString as XsdString
from pptx.oxml.xmlchemy import BaseOxmlElement as BaseOxmlElement, Choice as Choice, OneAndOnlyOne as OneAndOnlyOne, OptionalAttribute as OptionalAttribute, RequiredAttribute as RequiredAttribute, ZeroOrMore as ZeroOrMore, ZeroOrOne as ZeroOrOne, ZeroOrOneChoice as ZeroOrOneChoice

class _BaseSlideElement(BaseOxmlElement):
    @property
    def spTree(self): ...

class CT_Background(BaseOxmlElement):
    bgPr: Incomplete
    bgRef: Incomplete
    def add_noFill_bgPr(self): ...

class CT_BackgroundProperties(BaseOxmlElement):
    eg_fillProperties: Incomplete

class CT_CommonSlideData(BaseOxmlElement):
    bg: Incomplete
    spTree: Incomplete
    name: Incomplete
    def get_or_add_bgPr(self): ...

class CT_NotesMaster(_BaseSlideElement):
    cSld: Incomplete
    @classmethod
    def new_default(cls): ...

class CT_NotesSlide(_BaseSlideElement):
    cSld: Incomplete
    @classmethod
    def new(cls): ...

class CT_Slide(_BaseSlideElement):
    cSld: Incomplete
    clrMapOvr: Incomplete
    timing: Incomplete
    @classmethod
    def new(cls): ...
    @property
    def bg(self): ...
    def get_or_add_childTnLst(self): ...

class CT_SlideLayout(_BaseSlideElement):
    cSld: Incomplete

class CT_SlideLayoutIdList(BaseOxmlElement):
    sldLayoutId: Incomplete

class CT_SlideLayoutIdListEntry(BaseOxmlElement):
    rId: Incomplete

class CT_SlideMaster(_BaseSlideElement):
    cSld: Incomplete
    sldLayoutIdLst: Incomplete

class CT_SlideTiming(BaseOxmlElement):
    tnLst: Incomplete

class CT_TimeNodeList(BaseOxmlElement):
    def add_video(self, shape_id) -> None: ...

class CT_TLMediaNodeVideo(BaseOxmlElement):
    cMediaNode: Incomplete
