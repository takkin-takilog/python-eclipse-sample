# ==============================================================================
# brief        bokehのサンプル描写
#
# author       たっきん
#
# 事前準備 :
#     oandapyV20のインストール (pip install oandapyV20)
#     Bokehのインストール（conda install _bokeh）
# ==============================================================================

from bokeh.models import BoxEditTool, ColumnDataSource
from bokeh.plotting import figure, show, output_file

from bokehlib import bokeh_common as bc
import numpy as np


def draw_quadratic_curve(start, end):
    """2次曲線描写
    Args:
        start (int): x axis range of start.
        end (int): x axis range of end.
    Returns:
        xs (int): points of x element.
        ys (int): points of y element.
    """
    num = np.abs(end - start) + 1

    xs = np.linspace(start, end, num)
    ys = xs ** 2

    return xs, ys


def fig_sample01(tools, name):

    x_ax_typ = bc.AxisTyp.X_LINEAR
    set_title = "bokeh plot sample [" + name + "]"
    set_tools = "reset," + tools
    p = figure(x_axis_type=x_ax_typ, tools=set_tools, title=set_title)

    # ２次曲線描写
    xs, ys = draw_quadratic_curve(0, 20)
    p.line(xs, ys, line_width=2)
    p.circle(xs, ys, size=10)

    output_file_name = "out/bokeh_plot_sample_" + name + ".html"
    output_file(output_file_name, title=set_title)

    show(p)  # open a browser


def fig_sample02(name):

    x_ax_typ = bc.AxisTyp.X_LINEAR
    set_title = "bokeh plot sample [" + name + "]"

    set_tools = "reset"
    p = figure(x_axis_type=x_ax_typ, tools=set_tools, title=set_title)

    output_file_name = "out/bokeh_plot_sample_" + name + ".html"
    output_file(output_file_name, title=set_title)

    src = ColumnDataSource({
        'x': [5, 2, 8], 'y': [5, 7, 8], 'width': [2, 1, 2],
        'height': [2, 1, 1.5], 'alpha': [0.5, 0.5, 0.5]
    })

    renderer = p.rect('x', 'y', 'width', 'height', source=src, alpha='alpha')

    draw_tool = BoxEditTool(renderers=[renderer], empty_value=1)
    p.add_tools(draw_tool)
    p.toolbar.active_drag = draw_tool

    show(p)  # open a browser


if __name__ == "__main__":

    toolsstr = bc.ToolType.gen_str(bc.ToolType.PAN,
                                   bc.ToolType.XPAN,
                                   bc.ToolType.YPAN)
    fig_sample01(toolsstr, "pan")

    toolsstr = bc.ToolType.gen_str(bc.ToolType.WHEEL_ZOOM,
                                   bc.ToolType.XWHEEL_ZOOM,
                                   bc.ToolType.YWHEEL_ZOOM)
    fig_sample01(toolsstr, "wheel_zoom")

    toolsstr = bc.ToolType.gen_str(bc.ToolType.ZOOM_IN,
                                   bc.ToolType.ZOOM_OUT,
                                   bc.ToolType.XZOOM_IN,
                                   bc.ToolType.XZOOM_OUT,
                                   bc.ToolType.YZOOM_IN,
                                   bc.ToolType.YZOOM_OUT)
    fig_sample01(toolsstr, "zoom in-out")

    toolsstr = bc.ToolType.gen_str(bc.ToolType.CLICK,
                                   bc.ToolType.TAP)
    fig_sample01(toolsstr, "click-tap")

    toolsstr = bc.ToolType.gen_str(bc.ToolType.CROSSHAIR)
    fig_sample01(toolsstr, "crosshair")

    toolsstr = bc.ToolType.gen_str(bc.ToolType.BOX_SELECT,
                                   bc.ToolType.XBOX_SELECT,
                                   bc.ToolType.YBOX_SELECT)
    fig_sample01(toolsstr, "box_select")

    toolsstr = bc.ToolType.gen_str(bc.ToolType.POLY_SELECT,
                                   bc.ToolType.LASSO_SELECT)
    fig_sample01(toolsstr, "poly-lasso")

    toolsstr = bc.ToolType.gen_str(bc.ToolType.BOX_ZOOM,
                                   bc.ToolType.XBOX_ZOOM,
                                   bc.ToolType.YBOX_ZOOM)
    fig_sample01(toolsstr, "box_zoom")

    toolsstr = bc.ToolType.gen_str(bc.ToolType.HOVER)
    fig_sample01(toolsstr, "hover")

    toolsstr = bc.ToolType.gen_str(bc.ToolType.SAVE,
                                   bc.ToolType.PREVIEWSAVE)
    fig_sample01(toolsstr, "save")

    toolsstr = bc.ToolType.gen_str(bc.ToolType.UNDO,
                                   bc.ToolType.REDO)
    fig_sample01(toolsstr, "undo-redo")

    toolsstr = bc.ToolType.gen_str(bc.ToolType.HELP)
    fig_sample01(toolsstr, "help")

    toolsstr = bc.ToolType.gen_str(bc.ToolType.BOX_EDIT)
    fig_sample02("box_edit")

    toolsstr = bc.ToolType.gen_str(bc.ToolType.POLY_EDIT)
    fig_sample01(toolsstr, "poly_edit")

    toolsstr = bc.ToolType.gen_str(bc.ToolType.POINT_DRAW,
                                   bc.ToolType.POLY_DRAW)
    fig_sample01(toolsstr, "draw")
