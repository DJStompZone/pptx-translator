from _typeshed import Incomplete
from pptx.enum.base import EnumMember as EnumMember, Enumeration as Enumeration, ReturnValueOnlyEnumMember as ReturnValueOnlyEnumMember, XmlEnumeration as XmlEnumeration, XmlMappedEnumMember as XmlMappedEnumMember, alias as alias
from pptx.util import lazyproperty as lazyproperty

class MSO_AUTO_SHAPE_TYPE(XmlEnumeration):
    __ms_name__: str
    __url__: str
    __members__: Incomplete

class MSO_CONNECTOR_TYPE(XmlEnumeration):
    __ms_name__: str
    __url__: str
    __members__: Incomplete

class MSO_SHAPE_TYPE(Enumeration):
    __ms_name__: str
    __url__: str
    __members__: Incomplete

class PP_MEDIA_TYPE(Enumeration):
    __ms_name__: str
    __url__: str
    __members__: Incomplete

class PP_PLACEHOLDER_TYPE(XmlEnumeration):
    __ms_name__: str
    __url__: str
    __members__: Incomplete

class _ProgIdEnum:
    class Member:
        def __init__(self, name, progId, icon_filename, width, height) -> None: ...
        @property
        def height(self): ...
        @property
        def icon_filename(self): ...
        @property
        def progId(self): ...
        @property
        def width(self): ...
    def __contains__(self, item) -> bool: ...
    def DOCX(self): ...
    def PPTX(self): ...
    def XLSX(self): ...

PROG_ID: Incomplete
