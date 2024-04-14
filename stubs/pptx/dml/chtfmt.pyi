from ..shared import ElementProxy as ElementProxy
from ..util import lazyproperty as lazyproperty
from .fill import FillFormat as FillFormat
from .line import LineFormat as LineFormat

class ChartFormat(ElementProxy):
    def fill(self): ...
    def line(self): ...
