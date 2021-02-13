from matplotlib import cm
from matplotlib.colors import rgb2hex
import numpy as np

def get_colors_from_cmap(palette_name, n_colors=10, return_cm=False):
    colormap = cm.get_cmap(palette_name, n_colors)
    _colors = colormap(range(n_colors))
    colors = [rgb2hex(rgba) for rgba in _colors]
    if return_cm:
        return colors, colormap
    return colors


def get_colors_from_values(palette_name: str, values: list):
    # Normalize Values inside values list
    values = np.array(values)
    values = (values - min(values))*1.0/(max(values)-min(values))
    colormap = cm.get_cmap(palette_name)
    colors = colormap(values)
    return colors
