from ...enum.dml import MSO_THEME_COLOR as MSO_THEME_COLOR
from ..simpletypes import ST_HexColorRGB as ST_HexColorRGB, ST_Percentage as ST_Percentage
from ..xmlchemy import BaseOxmlElement as BaseOxmlElement, Choice as Choice, RequiredAttribute as RequiredAttribute, ZeroOrOne as ZeroOrOne, ZeroOrOneChoice as ZeroOrOneChoice
from _typeshed import Incomplete

class _BaseColorElement(BaseOxmlElement):
    lumMod: Incomplete
    lumOff: Incomplete
    def add_lumMod(self, value): ...
    def add_lumOff(self, value): ...
    def clear_lum(self): ...

class CT_Color(BaseOxmlElement):
    eg_colorChoice: Incomplete

class CT_HslColor(_BaseColorElement): ...

class CT_Percentage(BaseOxmlElement):
    val: Incomplete

class CT_PresetColor(_BaseColorElement): ...

class CT_SchemeColor(_BaseColorElement):
    val: Incomplete

class CT_ScRgbColor(_BaseColorElement): ...

class CT_SRgbColor(_BaseColorElement):
    val: Incomplete

class CT_SystemColor(_BaseColorElement): ...
