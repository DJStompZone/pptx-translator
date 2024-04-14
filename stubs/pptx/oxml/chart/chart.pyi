from _typeshed import Incomplete
from collections.abc import Generator
from pptx.oxml import parse_xml as parse_xml
from pptx.oxml.chart.shared import CT_Title as CT_Title
from pptx.oxml.ns import nsdecls as nsdecls, qn as qn
from pptx.oxml.simpletypes import ST_Style as ST_Style, XsdString as XsdString
from pptx.oxml.text import CT_TextBody as CT_TextBody
from pptx.oxml.xmlchemy import BaseOxmlElement as BaseOxmlElement, OneAndOnlyOne as OneAndOnlyOne, RequiredAttribute as RequiredAttribute, ZeroOrMore as ZeroOrMore, ZeroOrOne as ZeroOrOne

class CT_Chart(BaseOxmlElement):
    title: Incomplete
    autoTitleDeleted: Incomplete
    plotArea: Incomplete
    legend: Incomplete
    rId: Incomplete
    @property
    def has_legend(self): ...
    @has_legend.setter
    def has_legend(self, bool_value) -> None: ...
    @staticmethod
    def new_chart(rId): ...

class CT_ChartSpace(BaseOxmlElement):
    date1904: Incomplete
    style: Incomplete
    chart: Incomplete
    txPr: Incomplete
    externalData: Incomplete
    @property
    def catAx_lst(self): ...
    @property
    def date_1904(self): ...
    @property
    def dateAx_lst(self): ...
    def get_or_add_title(self): ...
    @property
    def plotArea(self): ...
    @property
    def valAx_lst(self): ...
    @property
    def xlsx_part_rId(self): ...

class CT_ExternalData(BaseOxmlElement):
    autoUpdate: Incomplete
    rId: Incomplete

class CT_PlotArea(BaseOxmlElement):
    catAx: Incomplete
    valAx: Incomplete
    def iter_sers(self) -> Generator[Incomplete, None, None]: ...
    def iter_xCharts(self) -> Generator[Incomplete, None, None]: ...
    @property
    def last_ser(self): ...
    @property
    def next_idx(self): ...
    @property
    def next_order(self): ...
    @property
    def sers(self): ...
    @property
    def xCharts(self): ...

class CT_Style(BaseOxmlElement):
    val: Incomplete
