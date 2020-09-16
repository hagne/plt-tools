

def add_position_of_interest2axes(ax, x = None, y = None, text = None, text_pos = (0.5,0.5), color = None, kwargs = None):
    """Plots a horizontal or vertical line and adds a text at the given position

    Parameters
    ----------
    ax
    x
    y
    text
    text_pos
    color
    kwargs

    Returns
    -------
    matplotlib.lines.Line2D
    matplotlib.text.Text
    """
    if not kwargs:
        kwargs = {}
    else:
        assert(type(kwargs) == dict)

    if color:
        kwargs['color'] = color

    if x and not y:
        g = ax.axvline(x=x, ymin=0, ymax=1, **kwargs)
        col = g.get_color()
        lw = g.get_linewidth()

    if y and not x:
        g = ax.axhline(y=y, xmin=0, xmax=1, **kwargs)
        col = g.get_color()
        lw = g.get_linewidth()

    if text:
        # if 'bbox' not in annotate_kwargs:
        #     annotate_kwargs['bbox'] = dict(boxstyle="round,pad=0.3", fc=[1, 1, 1, 0.8], ec=toi['color'], lw=1)
        # if 'ha' not in annotate_kwargs:
        #     annotate_kwargs['ha'] = 'center'
        # pos_y = annotate_kwargs.pop('pos_y')
        bbox = dict(boxstyle="round,pad=0.3", fc=[1, 1, 1, 1], ec = col, lw=lw)
        textinst = ax.text(text_pos[0], text_pos[1], text, ha = 'center', bbox=bbox)
        textinst.set_verticalalignment('center')
        # ax.annotate(annotate[0], (ts, annotate[1]), **annotate_kwargs)
        bboxinst  = textinst.get_bbox_patch()
    return g, textinst, bboxinst