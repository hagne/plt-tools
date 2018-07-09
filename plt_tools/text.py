import numpy as _np
import pandas as _pd

def get_angle_of_line_at_pos(data, x, aspectratio=1):
    """Returns the angle of the line at the given index"""
    try:
        px, py = data[data.x == x].iloc[0, :]
    except IndexError:
        raise IndexError('The postion is outside the date range ... adjust position to make this work')
    psx, psy = data.shift()[data.x == x].iloc[0, :]
    dx = px - psx
    dy = py - psy
    deg = _np.rad2deg(_np.arctan(dx / dy))
    print(deg)
    return deg


def get_interpolated_datapoint(x, y, position, axes='x', return_data=False):
    add_datapoint = position
    axes_alt = ['x', 'y']
    axes_alt.remove(axes)
    new_datapoint = {'y': [_np.nan], 'x': [_np.nan]}
    new_datapoint[axes] = add_datapoint

    data = _pd.DataFrame({'y': y, 'x': x})
    data = data.append(_pd.DataFrame(new_datapoint)).sort_values(axes)
    data.index = data[axes]
    data = data.interpolate(method='slinear')
    px, py = data.loc[add_datapoint, ['x', 'y']]
    if return_data:
        return px, py, data
    else:
        return px, py


def add_text_along_graph(graph, txt, position, axes='x'):
    a = graph._axes
    col = graph.get_color()
    xt, yt = graph.get_data()

    px, py, data = get_interpolated_datapoint(xt, yt, position, axes, return_data=True)
    bbox = {'boxstyle': 'round,pad=0.2'}
    txo = a.text(px, py, txt, va='center', ha='center', bbox=bbox)
    txo.set_rotation(get_angle_of_line_at_pos(data, px))
    boxo = txo.get_bbox_patch()
    boxo.set_linewidth(0.5)
    boxo.set_facecolor([1, 1, 1])
    boxo.set_edgecolor(col)
    return txo, boxo