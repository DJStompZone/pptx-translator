from pptx.dml.chtfmt import ChartFormat as ChartFormat
from pptx.enum.chart import XL_AXIS_CROSSES as XL_AXIS_CROSSES, XL_CATEGORY_TYPE as XL_CATEGORY_TYPE, XL_TICK_LABEL_POSITION as XL_TICK_LABEL_POSITION, XL_TICK_MARK as XL_TICK_MARK
from pptx.oxml.ns import qn as qn
from pptx.oxml.simpletypes import ST_Orientation as ST_Orientation
from pptx.shared import ElementProxy as ElementProxy
from pptx.text.text import Font as Font, TextFrame as TextFrame
from pptx.util import lazyproperty as lazyproperty

class _BaseAxis:
    def __init__(self, xAx) -> None: ...
    @property
    def axis_title(self): ...
    def format(self): ...
    @property
    def has_major_gridlines(self): ...
    @has_major_gridlines.setter
    def has_major_gridlines(self, value) -> None: ...
    @property
    def has_minor_gridlines(self): ...
    @has_minor_gridlines.setter
    def has_minor_gridlines(self, value) -> None: ...
    @property
    def has_title(self): ...
    @has_title.setter
    def has_title(self, value) -> None: ...
    def major_gridlines(self): ...
    @property
    def major_tick_mark(self): ...
    @major_tick_mark.setter
    def major_tick_mark(self, value) -> None: ...
    @property
    def maximum_scale(self): ...
    @maximum_scale.setter
    def maximum_scale(self, value) -> None: ...
    @property
    def minimum_scale(self): ...
    @minimum_scale.setter
    def minimum_scale(self, value) -> None: ...
    @property
    def minor_tick_mark(self): ...
    @minor_tick_mark.setter
    def minor_tick_mark(self, value) -> None: ...
    @property
    def reverse_order(self): ...
    @reverse_order.setter
    def reverse_order(self, value) -> None: ...
    def tick_labels(self): ...
    @property
    def tick_label_position(self): ...
    @tick_label_position.setter
    def tick_label_position(self, value) -> None: ...
    @property
    def visible(self): ...
    @visible.setter
    def visible(self, value) -> None: ...

class AxisTitle(ElementProxy):
    def __init__(self, title) -> None: ...
    def format(self): ...
    @property
    def has_text_frame(self): ...
    @has_text_frame.setter
    def has_text_frame(self, value) -> None: ...
    @property
    def text_frame(self): ...

class CategoryAxis(_BaseAxis):
    @property
    def category_type(self): ...

class DateAxis(_BaseAxis):
    @property
    def category_type(self): ...

class MajorGridlines(ElementProxy):
    def __init__(self, xAx) -> None: ...
    def format(self): ...

class TickLabels:
    def __init__(self, xAx_elm) -> None: ...
    def font(self): ...
    @property
    def number_format(self): ...
    @number_format.setter
    def number_format(self, value) -> None: ...
    @property
    def number_format_is_linked(self): ...
    @number_format_is_linked.setter
    def number_format_is_linked(self, value) -> None: ...
    @property
    def offset(self): ...
    @offset.setter
    def offset(self, value) -> None: ...

class ValueAxis(_BaseAxis):
    @property
    def crosses(self): ...
    @crosses.setter
    def crosses(self, value) -> None: ...
    @property
    def crosses_at(self): ...
    @crosses_at.setter
    def crosses_at(self, value) -> None: ...
    @property
    def major_unit(self): ...
    @major_unit.setter
    def major_unit(self, value) -> None: ...
    @property
    def minor_unit(self): ...
    @minor_unit.setter
    def minor_unit(self, value) -> None: ...