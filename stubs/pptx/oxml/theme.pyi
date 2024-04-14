from . import parse_from_template as parse_from_template
from .xmlchemy import BaseOxmlElement as BaseOxmlElement

class CT_OfficeStyleSheet(BaseOxmlElement):
    @classmethod
    def new_default(cls): ...
