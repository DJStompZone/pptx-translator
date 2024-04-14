from pptx.enum.shapes import MSO_SHAPE_TYPE as MSO_SHAPE_TYPE
from pptx.shapes.base import BaseShape as BaseShape
from pptx.shared import ParentedElementProxy as ParentedElementProxy
from pptx.spec import GRAPHIC_DATA_URI_CHART as GRAPHIC_DATA_URI_CHART, GRAPHIC_DATA_URI_OLEOBJ as GRAPHIC_DATA_URI_OLEOBJ, GRAPHIC_DATA_URI_TABLE as GRAPHIC_DATA_URI_TABLE
from pptx.table import Table as Table

class GraphicFrame(BaseShape):
    @property
    def chart(self): ...
    @property
    def chart_part(self): ...
    @property
    def has_chart(self): ...
    @property
    def has_table(self): ...
    @property
    def ole_format(self): ...
    @property
    def shadow(self) -> None: ...
    @property
    def shape_type(self): ...
    @property
    def table(self): ...

class _OleFormat(ParentedElementProxy):
    def __init__(self, graphicData, parent) -> None: ...
    @property
    def blob(self): ...
    @property
    def prog_id(self): ...
    @property
    def show_as_icon(self): ...