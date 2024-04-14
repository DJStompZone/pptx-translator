from ..compat import to_unicode as to_unicode
from ..enum.chart import XL_CHART_TYPE as XL_CHART_TYPE
from ..oxml import parse_xml as parse_xml
from ..oxml.ns import nsdecls as nsdecls

def ChartXmlWriter(chart_type, chart_data): ...
def SeriesXmlRewriterFactory(chart_type, chart_data): ...

class _BaseChartXmlWriter:
    def __init__(self, chart_type, series_seq) -> None: ...
    @property
    def xml(self) -> None: ...

class _BaseSeriesXmlWriter:
    def __init__(self, series, date_1904: bool = False) -> None: ...
    @property
    def name(self): ...
    def numRef_xml(self, wksht_ref, number_format, values): ...
    def pt_xml(self, values): ...
    @property
    def tx(self): ...
    @property
    def tx_xml(self): ...

class _BaseSeriesXmlRewriter:
    def __init__(self, chart_data) -> None: ...
    def replace_series_data(self, chartSpace) -> None: ...

class _AreaChartXmlWriter(_BaseChartXmlWriter):
    @property
    def xml(self): ...

class _BarChartXmlWriter(_BaseChartXmlWriter):
    @property
    def xml(self): ...

class _DoughnutChartXmlWriter(_BaseChartXmlWriter):
    @property
    def xml(self): ...

class _LineChartXmlWriter(_BaseChartXmlWriter):
    @property
    def xml(self): ...

class _PieChartXmlWriter(_BaseChartXmlWriter):
    @property
    def xml(self): ...

class _RadarChartXmlWriter(_BaseChartXmlWriter):
    @property
    def xml(self): ...

class _XyChartXmlWriter(_BaseChartXmlWriter):
    @property
    def xml(self): ...

class _BubbleChartXmlWriter(_XyChartXmlWriter):
    @property
    def xml(self): ...

class _CategorySeriesXmlWriter(_BaseSeriesXmlWriter):
    @property
    def cat(self): ...
    @property
    def cat_xml(self): ...
    @property
    def val(self): ...
    @property
    def val_xml(self): ...

class _XySeriesXmlWriter(_BaseSeriesXmlWriter):
    @property
    def xVal(self): ...
    @property
    def xVal_xml(self): ...
    @property
    def yVal(self): ...
    @property
    def yVal_xml(self): ...

class _BubbleSeriesXmlWriter(_XySeriesXmlWriter):
    @property
    def bubbleSize(self): ...
    @property
    def bubbleSize_xml(self): ...

class _BubbleSeriesXmlRewriter(_BaseSeriesXmlRewriter): ...
class _CategorySeriesXmlRewriter(_BaseSeriesXmlRewriter): ...
class _XySeriesXmlRewriter(_BaseSeriesXmlRewriter): ...
