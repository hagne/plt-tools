from mpl_toolkits.axes_grid1.inset_locator import inset_axes as _inset_axes


def colorbar_inside_plot(ax, mappable, extend = ('17%', '60%'), loc = 7, color_bg = [1, 1, 1, 0.5]):
    """
    Plots a colorbar inside the current plot.
    Parameters
    ----------
    ax: AxesSubplot
    mappable: mappable instance
        e.g. what is returned by imshow() or pcolormesh()
    extend: tuple
        The extend the colorbar is taking up of the underlying axis in %
    loc: int
        Location option as for legend see https://stackoverflow.com/questions/28521744/error-of-adding-a-legend-for-a-plot-in-python-3-2-matplotlib
    color_bg: what ever matplotlib excepts for colors
        Color of background.

    Returns
    -------
    Colorbar instance
    AxesHostAxes: Axis that containst the colorbar
    AxesHostAxes: Axis that makes up the background
    """

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
    cb=f.colorbar(mappable, cax=ax_cb) #make colorbar
    return cb, ax_cb, cbbox