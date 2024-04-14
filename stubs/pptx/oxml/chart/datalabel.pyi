from _typeshed import Incomplete
from pptx.enum.chart import XL_DATA_LABEL_POSITION as XL_DATA_LABEL_POSITION
from pptx.oxml import parse_xml as parse_xml
from pptx.oxml.ns import nsdecls as nsdecls
from pptx.oxml.text import CT_TextBody as CT_TextBody
from pptx.oxml.xmlchemy import BaseOxmlElement as BaseOxmlElement, OneAndOnlyOne as OneAndOnlyOne, RequiredAttribute as RequiredAttribute, ZeroOrMore as ZeroOrMore, ZeroOrOne as ZeroOrOne

class CT_DLbl(BaseOxmlElement):
    idx: Incomplete
    tx: Incomplete
    spPr: Incomplete
    txPr: Incomplete
    dLblPos: Incomplete
    def get_or_add_rich(self): ...
    def get_or_add_tx_rich(self): ...
    @property
    def idx_val(self): ...
    @classmethod
    def new_dLbl(cls): ...
    def remove_tx_rich(self) -> None: ...

class CT_DLblPos(BaseOxmlElement):
    val: Incomplete

class CT_DLbls(BaseOxmlElement):
    dLbl: Incomplete
    numFmt: Incomplete
    txPr: Incomplete
    dLblPos: Incomplete
    showLegendKey: Incomplete
    showVal: Incomplete
    showCatName: Incomplete
    showSerName: Incomplete
    showPercent: Incomplete
    @property
    def defRPr(self): ...
    def get_dLbl_for_point(self, idx): ...
    def get_or_add_dLbl_for_point(self, idx): ...
    @classmethod
    def new_dLbls(cls): ...
