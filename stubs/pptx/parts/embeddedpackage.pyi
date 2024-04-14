from _typeshed import Incomplete
from pptx.enum.shapes import PROG_ID as PROG_ID
from pptx.opc.package import Part as Part

class EmbeddedPackagePart(Part):
    @classmethod
    def factory(cls, prog_id, object_blob, package): ...
    @classmethod
    def new(cls, blob, package): ...

class EmbeddedDocxPart(EmbeddedPackagePart):
    partname_template: str
    content_type: Incomplete

class EmbeddedPptxPart(EmbeddedPackagePart):
    partname_template: str
    content_type: Incomplete

class EmbeddedXlsxPart(EmbeddedPackagePart):
    partname_template: str
    content_type: Incomplete
