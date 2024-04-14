from pptx.opc.package import Part as Part
from pptx.util import lazyproperty as lazyproperty

class MediaPart(Part):
    @classmethod
    def new(cls, package, media): ...
    def sha1(self): ...
