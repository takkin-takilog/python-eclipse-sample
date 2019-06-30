import numpy as np
from bokeh.plotting import figure
from bokeh.layouts import gridplot, row, column, layout, widgetbox
import matplotlib.pyplot as plt
from bokeh.io import show


N = 20
img = np.empty((N, N), dtype=np.uint32)
view = img.view(dtype=np.uint8).reshape((N, N, 4))
for i in range(N):
    for j in range(N):
        view[i, j, 0] = int(255 * i / N)
        view[i, j, 1] = 158
        view[i, j, 2] = int(255 * j / N)
        view[i, j, 3] = 255

#output_file("grid.html", )

p1 = figure(plot_width=150, plot_height=200, x_range=(0, 10), y_range=(0, 10))
p2 = figure(plot_width=150, plot_height=200, x_range=(0, 10), y_range=(0, 10))
p3 = figure(plot_width=400, plot_height=200, sizing_mode='stretch_width')

p1.image_rgba(image=[img], x=[0], y=[0], dw=[10], dh=[10])
p2.image_rgba(image=[img], x=[0], y=[0], dw=[10], dh=[10])
p3.line([1, 2, 3, 4, 5], np.array([6, 7, 2, 4, 5]) * 10000, line_width=2)
p3.xaxis.axis_label = f'Wavelength'
p3.yaxis.axis_label = f'Flux'

lay = row(
    [p1, p2, p3])
#    [p1, p2, p3], sizing_mode='fixed')
#    [p1, p2, p3], sizing_mode='stretch_width')
#    [p1, p2, p3], sizing_mode='stretch_both')
#    [p1, p2, p3], sizing_mode='scale_width')
#    [p1, p2, p3], sizing_mode='scale_both')


show(lay)
