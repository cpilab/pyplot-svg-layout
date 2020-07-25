import numpy as np
import matplotlib.pyplot as plt
from os.path import join, dirname, abspath
from sys import path
path.append(dirname(dirname(abspath(__file__))))    # adds parent directory to path to run this script from commandline

import svg_layout
from svg_layout import Panel, PanelLabel, Figure


def mpl_plot(ax: plt.Axes):
    """ An example pyplot plotting function for panel B and C.
    :param ax: a pyplot axis to be plot onto.
    """
    ax.plot(np.linspace(0, 1, 100), np.linspace(1, 3, 100))     # y = 2x+1 for x \in [0,1]


if __name__ == '__main__':
    """ A demo. """
    svg_layout.working_dir = join(abspath(dirname(__file__)), 'figs')
    # please specify the working directory first, which all input and output SVG file paths are relative to
    svg_layout.unit = 'cm'  # optional to specify the unit of length for width, height, x, and y inputs, default to cm
    # only five units of length are implemented: 'px' - pixel, 'in' - inch, 'cm' - centimeter, 'pc' - pica, 'pt' - point

    panels = [      # please give the layout as a list of Panel objects
        Panel(path='inkscape.svg', x=0.4, y=0.4, w=4, h=4, plotting_function=None, keep_aspect_ratio=True),
        Panel('pyplot_B.svg', 4.8, 0.4, 4, 4, mpl_plot, False),
        Panel('pyplot.svg', 0.4, 4.8, 8.4, 4, mpl_plot),
        Panel('inkscape.svg', 9.2, 0.4, 4, 8.4),
    ]   # trick: remove ``plotting function`` for pyplot panels where replotting is not necessary or too time-consuming.

    style = {'font-size': '18', 'font-family': 'Arial, sans-serif', "font-weight": 'bold'}  # fontsize in pt, as a str
    # See https://www.w3.org/TR/SVG11/styling.html#StyleAttribute for valid styling attributes.
    labels = PanelLabel.generate_labels(len(panels), dx=-0.2, dy=0.2, style=style)
    # automatically labels the panels as 'A', 'B', 'C', 'D'; can also manually create a PanelLabel list for flexibility.

    Figure(14, 9.2, panels, labels).plot('output.svg')  # see /figs/output.svg
