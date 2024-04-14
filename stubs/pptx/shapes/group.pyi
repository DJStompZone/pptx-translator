from pptx.dml.effect import ShadowFormat as ShadowFormat
from pptx.enum.shapes import MSO_SHAPE_TYPE as MSO_SHAPE_TYPE
from pptx.shapes.base import BaseShape as BaseShape
from pptx.util import lazyproperty as lazyproperty

class GroupShape(BaseShape):
    @property
    def click_action(self) -> None: ...
    @property
    def has_text_frame(self): ...
    def shadow(self): ...
    @property
    def shape_type(self): ...
    def shapes(self): ...
