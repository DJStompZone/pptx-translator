from ..oxml import parse_xml as parse_xml, register_element_cls as register_element_cls
from ..oxml.simpletypes import ST_ContentType as ST_ContentType, ST_Extension as ST_Extension, ST_TargetMode as ST_TargetMode, XsdAnyUri as XsdAnyUri, XsdId as XsdId
from ..oxml.xmlchemy import BaseOxmlElement as BaseOxmlElement, OptionalAttribute as OptionalAttribute, RequiredAttribute as RequiredAttribute, ZeroOrMore as ZeroOrMore
from _typeshed import Incomplete

nsmap: Incomplete

def oxml_tostring(elm, encoding: Incomplete | None = None, pretty_print: bool = False, standalone: Incomplete | None = None): ...
def serialize_part_xml(part_elm): ...

class CT_Default(BaseOxmlElement):
    extension: Incomplete
    contentType: Incomplete

class CT_Override(BaseOxmlElement):
    partName: Incomplete
    contentType: Incomplete

class CT_Relationship(BaseOxmlElement):
    rId: Incomplete
    reltype: Incomplete
    target_ref: Incomplete
    targetMode: Incomplete
    @classmethod
    def new(cls, rId, reltype, target, target_mode=...): ...

class CT_Relationships(BaseOxmlElement):
    relationship: Incomplete
    def add_rel(self, rId, reltype, target, is_external: bool = False) -> None: ...
    @classmethod
    def new(cls): ...
    @property
    def xml(self): ...

class CT_Types(BaseOxmlElement):
    default: Incomplete
    override: Incomplete
    def add_default(self, ext, content_type): ...
    def add_override(self, partname, content_type): ...
    @classmethod
    def new(cls): ...
