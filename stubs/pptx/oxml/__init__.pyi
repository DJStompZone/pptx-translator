from .action import CT_Hyperlink as CT_Hyperlink
from .chart.axis import CT_AxisUnit as CT_AxisUnit, CT_CatAx as CT_CatAx, CT_ChartLines as CT_ChartLines, CT_Crosses as CT_Crosses, CT_DateAx as CT_DateAx, CT_LblOffset as CT_LblOffset, CT_Orientation as CT_Orientation, CT_Scaling as CT_Scaling, CT_TickLblPos as CT_TickLblPos, CT_TickMark as CT_TickMark, CT_ValAx as CT_ValAx
from .chart.chart import CT_Chart as CT_Chart, CT_ChartSpace as CT_ChartSpace, CT_ExternalData as CT_ExternalData, CT_PlotArea as CT_PlotArea, CT_Style as CT_Style
from .chart.datalabel import CT_DLbl as CT_DLbl, CT_DLblPos as CT_DLblPos, CT_DLbls as CT_DLbls
from .chart.legend import CT_Legend as CT_Legend, CT_LegendPos as CT_LegendPos
from .chart.marker import CT_Marker as CT_Marker, CT_MarkerSize as CT_MarkerSize, CT_MarkerStyle as CT_MarkerStyle
from .chart.plot import CT_Area3DChart as CT_Area3DChart, CT_AreaChart as CT_AreaChart, CT_BarChart as CT_BarChart, CT_BarDir as CT_BarDir, CT_BubbleChart as CT_BubbleChart, CT_BubbleScale as CT_BubbleScale, CT_DoughnutChart as CT_DoughnutChart, CT_GapAmount as CT_GapAmount, CT_Grouping as CT_Grouping, CT_LineChart as CT_LineChart, CT_Overlap as CT_Overlap, CT_PieChart as CT_PieChart, CT_RadarChart as CT_RadarChart, CT_ScatterChart as CT_ScatterChart
from .chart.series import CT_AxDataSource as CT_AxDataSource, CT_DPt as CT_DPt, CT_Lvl as CT_Lvl, CT_NumDataSource as CT_NumDataSource, CT_SeriesComposite as CT_SeriesComposite, CT_StrVal_NumVal_Composite as CT_StrVal_NumVal_Composite
from .chart.shared import CT_Boolean as CT_Boolean, CT_Boolean_Explicit as CT_Boolean_Explicit, CT_Double as CT_Double, CT_Layout as CT_Layout, CT_LayoutMode as CT_LayoutMode, CT_ManualLayout as CT_ManualLayout, CT_NumFmt as CT_NumFmt, CT_Title as CT_Title, CT_Tx as CT_Tx, CT_UnsignedInt as CT_UnsignedInt
from .coreprops import CT_CoreProperties as CT_CoreProperties
from .dml.color import CT_Color as CT_Color, CT_HslColor as CT_HslColor, CT_Percentage as CT_Percentage, CT_PresetColor as CT_PresetColor, CT_SRgbColor as CT_SRgbColor, CT_ScRgbColor as CT_ScRgbColor, CT_SchemeColor as CT_SchemeColor, CT_SystemColor as CT_SystemColor
from .dml.fill import CT_Blip as CT_Blip, CT_BlipFillProperties as CT_BlipFillProperties, CT_GradientFillProperties as CT_GradientFillProperties, CT_GradientStop as CT_GradientStop, CT_GradientStopList as CT_GradientStopList, CT_GroupFillProperties as CT_GroupFillProperties, CT_LinearShadeProperties as CT_LinearShadeProperties, CT_NoFillProperties as CT_NoFillProperties, CT_PatternFillProperties as CT_PatternFillProperties, CT_RelativeRect as CT_RelativeRect, CT_SolidColorFillProperties as CT_SolidColorFillProperties
from .dml.line import CT_PresetLineDashProperties as CT_PresetLineDashProperties
from .ns import NamespacePrefixedTag as NamespacePrefixedTag
from .presentation import CT_Presentation as CT_Presentation, CT_SlideId as CT_SlideId, CT_SlideIdList as CT_SlideIdList, CT_SlideMasterIdList as CT_SlideMasterIdList, CT_SlideMasterIdListEntry as CT_SlideMasterIdListEntry, CT_SlideSize as CT_SlideSize
from .shapes.autoshape import CT_AdjPoint2D as CT_AdjPoint2D, CT_CustomGeometry2D as CT_CustomGeometry2D, CT_GeomGuide as CT_GeomGuide, CT_GeomGuideList as CT_GeomGuideList, CT_NonVisualDrawingShapeProps as CT_NonVisualDrawingShapeProps, CT_Path2D as CT_Path2D, CT_Path2DClose as CT_Path2DClose, CT_Path2DLineTo as CT_Path2DLineTo, CT_Path2DList as CT_Path2DList, CT_Path2DMoveTo as CT_Path2DMoveTo, CT_PresetGeometry2D as CT_PresetGeometry2D, CT_Shape as CT_Shape, CT_ShapeNonVisual as CT_ShapeNonVisual
from .shapes.connector import CT_Connection as CT_Connection, CT_Connector as CT_Connector, CT_ConnectorNonVisual as CT_ConnectorNonVisual, CT_NonVisualConnectorProperties as CT_NonVisualConnectorProperties
from .shapes.graphfrm import CT_GraphicalObject as CT_GraphicalObject, CT_GraphicalObjectData as CT_GraphicalObjectData, CT_GraphicalObjectFrame as CT_GraphicalObjectFrame, CT_GraphicalObjectFrameNonVisual as CT_GraphicalObjectFrameNonVisual, CT_OleObject as CT_OleObject
from .shapes.groupshape import CT_GroupShape as CT_GroupShape, CT_GroupShapeNonVisual as CT_GroupShapeNonVisual, CT_GroupShapeProperties as CT_GroupShapeProperties
from .shapes.picture import CT_Picture as CT_Picture, CT_PictureNonVisual as CT_PictureNonVisual
from .shapes.shared import CT_ApplicationNonVisualDrawingProps as CT_ApplicationNonVisualDrawingProps, CT_LineProperties as CT_LineProperties, CT_NonVisualDrawingProps as CT_NonVisualDrawingProps, CT_Placeholder as CT_Placeholder, CT_Point2D as CT_Point2D, CT_PositiveSize2D as CT_PositiveSize2D, CT_ShapeProperties as CT_ShapeProperties, CT_Transform2D as CT_Transform2D
from .slide import CT_Background as CT_Background, CT_BackgroundProperties as CT_BackgroundProperties, CT_CommonSlideData as CT_CommonSlideData, CT_NotesMaster as CT_NotesMaster, CT_NotesSlide as CT_NotesSlide, CT_Slide as CT_Slide, CT_SlideLayout as CT_SlideLayout, CT_SlideLayoutIdList as CT_SlideLayoutIdList, CT_SlideLayoutIdListEntry as CT_SlideLayoutIdListEntry, CT_SlideMaster as CT_SlideMaster, CT_SlideTiming as CT_SlideTiming, CT_TLMediaNodeVideo as CT_TLMediaNodeVideo, CT_TimeNodeList as CT_TimeNodeList
from .table import CT_Table as CT_Table, CT_TableCell as CT_TableCell, CT_TableCellProperties as CT_TableCellProperties, CT_TableCol as CT_TableCol, CT_TableGrid as CT_TableGrid, CT_TableProperties as CT_TableProperties, CT_TableRow as CT_TableRow
from .text import CT_RegularTextRun as CT_RegularTextRun, CT_TextBody as CT_TextBody, CT_TextBodyProperties as CT_TextBodyProperties, CT_TextCharacterProperties as CT_TextCharacterProperties, CT_TextField as CT_TextField, CT_TextFont as CT_TextFont, CT_TextLineBreak as CT_TextLineBreak, CT_TextNormalAutofit as CT_TextNormalAutofit, CT_TextParagraph as CT_TextParagraph, CT_TextParagraphProperties as CT_TextParagraphProperties, CT_TextSpacing as CT_TextSpacing, CT_TextSpacingPercent as CT_TextSpacingPercent, CT_TextSpacingPoint as CT_TextSpacingPoint
from .theme import CT_OfficeStyleSheet as CT_OfficeStyleSheet
from _typeshed import Incomplete

element_class_lookup: Incomplete
oxml_parser: Incomplete

def parse_from_template(template_name): ...
def parse_xml(xml): ...
def register_element_cls(nsptagname, cls) -> None: ...
