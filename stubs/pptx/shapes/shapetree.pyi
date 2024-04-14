from _typeshed import Incomplete
from pptx.compat import BytesIO as BytesIO
from pptx.enum.shapes import PP_PLACEHOLDER as PP_PLACEHOLDER, PROG_ID as PROG_ID
from pptx.media import SPEAKER_IMAGE_BYTES as SPEAKER_IMAGE_BYTES, Video as Video
from pptx.oxml.ns import qn as qn
from pptx.oxml.shapes.graphfrm import CT_GraphicalObjectFrame as CT_GraphicalObjectFrame
from pptx.oxml.shapes.picture import CT_Picture as CT_Picture
from pptx.oxml.simpletypes import ST_Direction as ST_Direction
from pptx.shapes.autoshape import AutoShapeType as AutoShapeType, Shape as Shape
from pptx.shapes.base import BaseShape as BaseShape
from pptx.shapes.connector import Connector as Connector
from pptx.shapes.freeform import FreeformBuilder as FreeformBuilder
from pptx.shapes.graphfrm import GraphicFrame as GraphicFrame
from pptx.shapes.group import GroupShape as GroupShape
from pptx.shapes.picture import Movie as Movie, Picture as Picture
from pptx.shapes.placeholder import ChartPlaceholder as ChartPlaceholder, LayoutPlaceholder as LayoutPlaceholder, MasterPlaceholder as MasterPlaceholder, NotesSlidePlaceholder as NotesSlidePlaceholder, PicturePlaceholder as PicturePlaceholder, PlaceholderGraphicFrame as PlaceholderGraphicFrame, PlaceholderPicture as PlaceholderPicture, SlidePlaceholder as SlidePlaceholder, TablePlaceholder as TablePlaceholder
from pptx.shared import ParentedElementProxy as ParentedElementProxy
from pptx.util import Emu as Emu, lazyproperty as lazyproperty

class _BaseShapes(ParentedElementProxy):
    def __init__(self, spTree, parent) -> None: ...
    def __getitem__(self, idx): ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def clone_placeholder(self, placeholder) -> None: ...
    def ph_basename(self, ph_type): ...
    @property
    def turbo_add_enabled(self): ...
    @turbo_add_enabled.setter
    def turbo_add_enabled(self, value) -> None: ...

class _BaseGroupShapes(_BaseShapes):
    def __init__(self, grpSp, parent) -> None: ...
    def add_chart(self, chart_type, x, y, cx, cy, chart_data): ...
    def add_connector(self, connector_type, begin_x, begin_y, end_x, end_y): ...
    def add_group_shape(self, shapes=[]): ...
    def add_ole_object(self, object_file, prog_id, left, top, width: Incomplete | None = None, height: Incomplete | None = None, icon_file: Incomplete | None = None, icon_width: Incomplete | None = None, icon_height: Incomplete | None = None): ...
    def add_picture(self, image_file, left, top, width: Incomplete | None = None, height: Incomplete | None = None): ...
    def add_shape(self, autoshape_type_id, left, top, width, height): ...
    def add_textbox(self, left, top, width, height): ...
    def build_freeform(self, start_x: int = 0, start_y: int = 0, scale: float = 1.0): ...
    def index(self, shape): ...

class GroupShapes(_BaseGroupShapes): ...

class SlideShapes(_BaseGroupShapes):
    def add_movie(self, movie_file, left, top, width, height, poster_frame_image: Incomplete | None = None, mime_type=...): ...
    def add_table(self, rows, cols, left, top, width, height): ...
    def clone_layout_placeholders(self, slide_layout) -> None: ...
    @property
    def placeholders(self): ...
    @property
    def title(self): ...

class LayoutShapes(_BaseShapes): ...
class MasterShapes(_BaseShapes): ...

class NotesSlideShapes(_BaseShapes):
    def ph_basename(self, ph_type): ...

class BasePlaceholders(_BaseShapes): ...

class LayoutPlaceholders(BasePlaceholders):
    def get(self, idx, default: Incomplete | None = None): ...

class MasterPlaceholders(BasePlaceholders):
    def get(self, ph_type, default: Incomplete | None = None): ...

class NotesSlidePlaceholders(MasterPlaceholders): ...

class SlidePlaceholders(ParentedElementProxy):
    def __getitem__(self, idx): ...
    def __iter__(self): ...
    def __len__(self) -> int: ...

def BaseShapeFactory(shape_elm, parent): ...
def SlideShapeFactory(shape_elm, parent): ...

class _MoviePicElementCreator:
    def __init__(self, shapes, shape_id, movie_file, x, y, cx, cy, poster_frame_file, mime_type) -> None: ...
    @classmethod
    def new_movie_pic(cls, shapes, shape_id, movie_file, x, y, cx, cy, poster_frame_image, mime_type): ...

class _OleObjectElementCreator:
    def __init__(self, shapes, shape_id, ole_object_file, prog_id, x, y, cx, cy, icon_file, icon_width, icon_height) -> None: ...
    @classmethod
    def graphicFrame(cls, shapes, shape_id, ole_object_file, prog_id, x, y, cx, cy, icon_file, icon_width, icon_height): ...