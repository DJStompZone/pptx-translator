from _typeshed import Incomplete
from pptx.oxml import parse_xml as parse_xml
from pptx.oxml.ns import nsdecls as nsdecls
from pptx.oxml.simpletypes import ST_LayoutMode as ST_LayoutMode, XsdBoolean as XsdBoolean, XsdDouble as XsdDouble, XsdString as XsdString, XsdUnsignedInt as XsdUnsignedInt
from pptx.oxml.xmlchemy import BaseOxmlElement as BaseOxmlElement, OptionalAttribute as OptionalAttribute, RequiredAttribute as RequiredAttribute, ZeroOrOne as ZeroOrOne

class CT_Boolean(BaseOxmlElement):
    val: Incomplete

class CT_Boolean_Explicit(BaseOxmlElement):
    @property
    def val(self): ...
    @val.setter
    def val(self, value) -> None: ...

class CT_Double(BaseOxmlElement):
    val: Incomplete

class CT_Layout(BaseOxmlElement):
    manualLayout: Incomplete
    @property
    def horz_offset(self): ...
    @horz_offset.setter
    def horz_offset(self, offset) -> None: ...

class CT_LayoutMode(BaseOxmlElement):
    val: Incomplete

class CT_ManualLayout(BaseOxmlElement):
    xMode: Incomplete
    x: Incomplete
    @property
    def horz_offset(self): ...
    @horz_offset.setter
    def horz_offset(self, offset) -> None: ...

class CT_NumFmt(BaseOxmlElement):
    formatCode: Incomplete
    sourceLinked: Incomplete

class CT_Title(BaseOxmlElement):
    tx: Incomplete
    spPr: Incomplete
    def get_or_add_tx_rich(self): ...
    @property
    def tx_rich(self): ...
    @staticmethod
    def new_title(): ...

class CT_Tx(BaseOxmlElement):
    strRef: Incomplete
    rich: Incomplete

class CT_UnsignedInt(BaseOxmlElement):
    val: Incomplete
