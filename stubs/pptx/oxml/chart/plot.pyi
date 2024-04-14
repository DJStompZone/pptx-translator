from ..simpletypes import ST_BarDir as ST_BarDir, ST_BubbleScale as ST_BubbleScale, ST_GapAmount as ST_GapAmount, ST_Grouping as ST_Grouping, ST_Overlap as ST_Overlap
from ..xmlchemy import BaseOxmlElement as BaseOxmlElement, OneAndOnlyOne as OneAndOnlyOne, OptionalAttribute as OptionalAttribute, ZeroOrMore as ZeroOrMore, ZeroOrOne as ZeroOrOne
from .datalabel import CT_DLbls as CT_DLbls
from _typeshed import Incomplete

class BaseChartElement(BaseOxmlElement):
    @property
    def cat(self): ...
    @property
    def cat_pt_count(self): ...
    @property
    def cat_pts(self): ...
    @property
    def grouping_val(self): ...
    def iter_sers(self): ...
    @property
    def sers(self): ...

class CT_Area3DChart(BaseChartElement):
    grouping: Incomplete

class CT_AreaChart(BaseChartElement):
    grouping: Incomplete
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete

class CT_BarChart(BaseChartElement):
    barDir: Incomplete
    grouping: Incomplete
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete
    gapWidth: Incomplete
    overlap: Incomplete
    @property
    def grouping_val(self): ...

class CT_BarDir(BaseOxmlElement):
    val: Incomplete

class CT_BubbleChart(BaseChartElement):
    ser: Incomplete
    dLbls: Incomplete
    bubble3D: Incomplete
    bubbleScale: Incomplete

class CT_BubbleScale(BaseChartElement):
    val: Incomplete

class CT_DoughnutChart(BaseChartElement):
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete

class CT_GapAmount(BaseOxmlElement):
    val: Incomplete

class CT_Grouping(BaseOxmlElement):
    val: Incomplete

class CT_LineChart(BaseChartElement):
    grouping: Incomplete
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete

class CT_Overlap(BaseOxmlElement):
    val: Incomplete

class CT_PieChart(BaseChartElement):
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete

class CT_RadarChart(BaseChartElement):
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete

class CT_ScatterChart(BaseChartElement):
    varyColors: Incomplete
    ser: Incomplete
