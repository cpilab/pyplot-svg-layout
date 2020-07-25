# SVG layout tool for pyplot
Having a script able to generate an exact figure in a publication is good for open science.
However, if you manually draw a panel, 
it is not easy to incorporate it into the figure using matplotlib.pyplot.
If you, like me, find converting an SVG/PDF to PNG/JPG mysteriously unsettling, try this. 

``svg_layout.py`` combines manually-drawn SVG panels (e.g. Inkscape SVGs) and 
pyplot-plotted SVG panels into an entire figure, 
with straightforward layout and labeling options.

To get started with an example, run ``demo/demo.py``.
