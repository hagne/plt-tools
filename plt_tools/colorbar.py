from mpl_toolkits.axes_grid1.inset_locator import inset_axes as _inset_axes


def colorbar_inside_plot(ax, im, extend = ('17%', '60%'), loc = 7, color_bg = [1,1,1,0.5]):

    # first insert that acts as a background of the colorbar ... so you can see the text on the underlying plot
    cbbox = _inset_axes(ax, extend[0], extend[1], loc = loc)
    [cbbox.spines[k].set_visible(False) for k in cbbox.spines]  # remove axes
    cbbox.tick_params(axis='both',
                      left='off',
                      top='off',
                      right='off',
                      bottom='off',
                      labelleft='off',
                      labeltop='off',
                      labelright='off',
                      labelbottom='off')                        # remove ticks

    cbbox.set_facecolor(color_bg)                            # make transparent
    cbbox.grid(False)

    # second insert that will be filled by the colorbar
    ax_cb = _inset_axes(cbbox, '25%', '90%', loc = 6)
    f = ax.get_figure()
    cb=f.colorbar(im,cax=ax_cb) #make colorbar
    return cb, cbbox, ax_cb