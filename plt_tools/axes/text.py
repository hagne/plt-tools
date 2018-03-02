import matplotlib.pylab as _plt
from string import ascii_lowercase as _ascii_lowercase

def set_subplots_labels(a, pos = (0.06, 0.9), cycle_start = 0, bbox_lw = None):
    if type(a).__name__ == 'AxesSubplot':
        a = [a]
    abc = ['({})'.format(c) for c in _ascii_lowercase]#['(a)', '(b)','(c)', '(b)','(c)', '(b)','(c)', '(b)','(c)', '(b)','(c)', '(b)','(c)']
    texts = []
    boxes = []
    for e, at in enumerate(a):
        bbox = {}
        bbox['fc'] = [1,1,1,0.7]
        bbox['ec'] = 'black'
        bbox['boxstyle'] = 'round'
        txtat = at.text(pos[0], pos[1], abc[e + cycle_start], fontsize='large', transform = at.transAxes, bbox = bbox)
        bbp=txtat.get_bbox_patch()
        if not bbox_lw:
            bbox_lw = _plt.rcParams['axes.linewidth']
        bbp.set_linewidth(bbox_lw)
        texts.append(txtat)
        boxes.append(bbp)
    return texts, boxes