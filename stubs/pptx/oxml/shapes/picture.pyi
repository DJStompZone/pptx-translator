from _typeshed import Incomplete
from pptx.oxml import parse_xml as parse_xml
from pptx.oxml.ns import nsdecls as nsdecls
from pptx.oxml.shapes.shared import BaseShapeElement as BaseShapeElement
from pptx.oxml.xmlchemy import BaseOxmlElement as BaseOxmlElement, OneAndOnlyOne as OneAndOnlyOne

class CT_Picture(BaseShapeElement):
    nvPicPr: Incomplete
    blipFill: Incomplete
    spPr: Incomplete
    @property
    def blip_rId(self): ...
    def crop_to_fit(self, image_size, view_size) -> None: ...
    def get_or_add_ln(self): ...
    @property
    def ln(self): ...
    @classmethod
    def new_ph_pic(cls, id_, name, desc, rId): ...
    @classmethod
    def new_pic(cls, shape_id, name, desc, rId, x, y, cx, cy): ...
    @classmethod
    def new_video_pic(cls, shape_id, shape_name, video_rId, media_rId, poster_frame_rId, x, y, cx, cy): ...
    @property
    def srcRect_b(self): ...
    @srcRect_b.setter
    def srcRect_b(self, value) -> None: ...
    @property
    def srcRect_l(self): ...
    @srcRect_l.setter
    def srcRect_l(self, value) -> None: ...
    @property
    def srcRect_r(self): ...
    @srcRect_r.setter
    def srcRect_r(self, value) -> None: ...
    @property
    def srcRect_t(self): ...
    @srcRect_t.setter
    def srcRect_t(self, value) -> None: ...

class CT_PictureNonVisual(BaseOxmlElement):
    cNvPr: Incomplete
    nvPr: Incomplete