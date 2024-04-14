from .simpletypes import XsdString as XsdString
from .xmlchemy import BaseOxmlElement as BaseOxmlElement, OptionalAttribute as OptionalAttribute
from _typeshed import Incomplete

class CT_Hyperlink(BaseOxmlElement):
    rId: Incomplete
    action: Incomplete
    @property
    def action_fields(self): ...
    @property
    def action_verb(self): ...
