from ..simpletypes import XsdUnsignedInt as XsdUnsignedInt
from ..xmlchemy import BaseOxmlElement as BaseOxmlElement, OneAndOnlyOne as OneAndOnlyOne, OxmlElement as OxmlElement, RequiredAttribute as RequiredAttribute, ZeroOrMore as ZeroOrMore, ZeroOrOne as ZeroOrOne
from .datalabel import CT_DLbls as CT_DLbls
from _typeshed import Incomplete

class CT_AxDataSource(BaseOxmlElement):
    multiLvlStrRef: Incomplete
    @property
    def lvls(self): ...

class CT_DPt(BaseOxmlElement):
    idx: Incomplete
    marker: Incomplete
    spPr: Incomplete
    @classmethod
    def new_dPt(cls): ...

class CT_Lvl(BaseOxmlElement):
    pt: Incomplete

class CT_NumDataSource(BaseOxmlElement):
    numRef: Incomplete
    @property
    def ptCount_val(self): ...
    def pt_v(self, idx): ...

class CT_SeriesComposite(BaseOxmlElement):
    idx: Incomplete
    order: Incomplete
    tx: Incomplete
    spPr: Incomplete
    invertIfNegative: Incomplete
    marker: Incomplete
    dPt: Incomplete
    dLbls: Incomplete
    cat: Incomplete
    val: Incomplete
    xVal: Incomplete
    yVal: Incomplete
    smooth: Incomplete
    bubbleSize: Incomplete
    @property
    def bubbleSize_ptCount_val(self): ...
    @property
    def cat_ptCount_val(self): ...
    def get_dLbl(self, idx): ...
    def get_or_add_dLbl(self, idx): ...
    def get_or_add_dPt_for_point(self, idx): ...
    @property
    def xVal_ptCount_val(self): ...
    @property
    def yVal_ptCount_val(self): ...

class CT_StrVal_NumVal_Composite(BaseOxmlElement):
    v: Incomplete
    idx: Incomplete
    @property
    def value(self): ...
