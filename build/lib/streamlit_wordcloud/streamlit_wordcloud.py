import os
import streamlit.components.v1 as components
import json
from typing import Union, List
from .utils import get_colors_from_cmap as get_colors

_RELEASE = True


if not _RELEASE:
    _wordcloud = components.declare_component(
        "wordcloud",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _wordcloud = components.declare_component(
        "wordcloud", path=build_dir
    )


def visualize(
    words: List[dict],
    width: str = None,
    height: str =None,
    font_min: int=None,
    font_max: int=None,
    font_scale: float=None,
    max_words: int=None,
    palette: str='viridis',
    per_word_coloring: bool= False,
    padding: int=None,
    layout: str='rectangular',
    enable_tooltip: bool= True,
    tooltip_data_fields: dict= {'text':'Word', 'value':'Count'},
    key: str=None,
) -> dict:
    """Create a new instance of "wordcloud".

    Parameters
    ----------
    words: list[dict]
        The list of words to be plotted in a wordcloud. Each word should be a
        dictionary containing the following keys:
            text: str
                [required] word to be displayed on the wordcloud
            value: int
                [required] size of the word
            color: str
                [optional] color of the word to be discplayed (Hex or RGB format). 
                Please note that these colors will only be used if `per_word_coloring` 
                parameter is set to True.
            <-meta-data->: UNION(str, int)
                [optional] For any additional meta data od interest, you can pass 
                separate keys. These additional keys will be returned in the return 
                `clicked` and `hovered` dictionaries. You can also use them when 
                specifying tooltip fields. For more info, refer to `tooltip_meta_fields` 
                parameter.

    width: str
        The width of wordcloud. By default, the width is '100%', i.e., it will fill the
        whole containing block. If you want the wordcloud to be responsive (to 
        change when window size changes), you should pass its relative size (100%, 
        90%, 80%, ...). Other valid examples: 100px, 200, 1.5em, 300pt, 10mm, ...
    
    height: str
        The height of wordcloud. Default is '100%'. Other valid examples: 100px, 
        200, 1.5em, 300pt, 10mm, ...
    
    font_min: int
        The smallest font size of words in the wordcloud.
    
    font_max: int
        The largest font size of words in the wordcloud.
    
    font_scale: float
        The scaling factor which will be multiplied by the default font sizes. Please
        note that the `font_scale` can only effects if no `font_min` or `font_max` has
        been passed. In case of passing `font_min` and `font_max`, only their absolute
        number will be effective.

    max_words: int
        The maximum number of words to be plotted on the wordcloud.

    palette: str
        The color palette to be used for the words in the wordcloud. Please note that 
        this value may only effect if no `color` key has been passed in the list of
        `words`. By default, the color palette is 'viridis'. You can pass any valid 
        Matplotlib Colormap (Please refer to the following link for the list of all
        color palettes: https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html ).

    per_word_coloring: bool
        If True, the `color` key in the `words` parameter will be used to fill the 
        words in the wordcloud.

    padding: int
        The padding between words in the word cloud. Default: 1 .

    layout: str
        The wordcloud layout. Available options: ['rectangular', 'archimedean']

    enable_tooltip: bool
        Whether to show tooltip popover once hover on a word.

    tooltip_data_fields: dict
        A dictionary containing all the fields and their displayed valued to be shown 
        in the tooltip. These fields can only be selected from the available keys 
        passed in the `words` parameter.

    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    Dict
        A dictionary containing information of the word that has been hovered or
        has been clicked.

    """
    palette_colors = get_colors(palette, 100)
    
    component_value = _wordcloud(
        words=words,
        width=width,
        height=height,
        fontMin=font_min,
        fontMax=font_max,
        fontScale=font_scale,
        maxWords=max_words,
        paletteColors=palette_colors,
        padding=padding,
        layout=layout,
        enableTooltip=enable_tooltip,
        tooltipDataFields=tooltip_data_fields,
        perWordColoring=per_word_coloring,
        key=key,
        default=None,
    )

    return component_value


# if not _RELEASE:
# import streamlit as st

# st.set_page_config(layout="wide")
# st.subheader("Component with constant args")

# words = [
#     dict(text="told", value=204, color="#b5de2b", country="US"),
#     dict(text="mistake", value=151, color="#b5de2b", country="DE"),
#     dict(text="thought", value=26, color="#b5de2b", country="UK"),
#     dict(text="bad", value=17, color="#b5de2b", country="UK"),
#     dict(text="NOT", value=227, color="#b5de2b", country="US"),
#     dict(text="WHY", value=57, color="#b5de2b", country="DE"),
#     dict(text="GO", value=107, color="#b5de2b", country="FR"),
#     dict(text="hospital", value=31, color="#b5de2b", country="FR"),
#     dict(text="eye", value=43, color="#b5de2b", country="US"),
#     dict(text="test", value=20, color="#b5de2b", country="US"),
#     dict(text="appointment", value=49, color="#b5de2b", country="US"),
# ]
# return_dict = visualize(words, tooltip_data_fields={
#     'text':'Word', 'value':'Count', 'country':'Country of Origin'
# }, per_word_coloring=False)
# st.markdown("You've clicked:\n\n {}".format(json.dumps(return_dict, indent=2)))

# st.markdown("---")
