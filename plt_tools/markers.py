

def add_position_of_interest2axes(ax, x = None, y = None, text = None, text_pos = (0.5,0.5), color = None, kwargs = None):
    if not kwargs:
        kwargs = {}
    else:
        assert(type(kwargs) == dict)

    if color:
        kwargs['color'] = color

    # if type(x) == dict:
    #     x = [x]
    # for toi in x:
    # ts = toi.pop('datetime')
    # if 'color' not in toi.keys():
    #     toi['color'] = 'black'
    # try:
    #     annotate = toi.pop('annotate')
    #     annotate_kwargs = toi.pop('annotate_kwargs')
    # except:
    #     annotate = None
    #
    # if 'vline_kwargs' not in toi.keys():
    #     toi['vline_kwargs'] = {}
    #
    # if 'color' not in toi['vline_kwargs'].keys():
    #     toi['vline_kwargs']['color'] = toi['color']


    if x and not y:
        g = ax.axvline(x=x, ymin=0, ymax=1, **kwargs)
        col = g.get_color()
        lw = g.get_linewidth()

    if text:
        # if 'bbox' not in annotate_kwargs:
        #     annotate_kwargs['bbox'] = dict(boxstyle="round,pad=0.3", fc=[1, 1, 1, 0.8], ec=toi['color'], lw=1)
        # if 'ha' not in annotate_kwargs:
        #     annotate_kwargs['ha'] = 'center'
        # pos_y = annotate_kwargs.pop('pos_y')
        bbox = dict(boxstyle="round,pad=0.3", fc=[1, 1, 1, 1], ec = col, lw=lw)
        ax.text(text_pos[0], text_pos[1], text, ha = 'center', bbox=bbox)

        # ax.annotate(annotate[0], (ts, annotate[1]), **annotate_kwargs)

    return g