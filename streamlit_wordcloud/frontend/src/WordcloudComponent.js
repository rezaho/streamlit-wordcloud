import { Streamlit, withStreamlitConnection } from "streamlit-component-lib"
import React, { useState, useEffect } from "react"
import ReactWordCloud from "react-wordcloud"
import "tippy.js/dist/tippy.css"
import "tippy.js/animations/scale.css"
import "tippy.js/themes/light.css"

const initialSettings = {
  width: "100%",
  height: "100%",
  fontScale: 1.0,
  fontMin: 8,
  fontMax: 72,
  padding: 1,
  enableTooltip: true,
  spiral: "rectangular",
  scale: "linear",
  tooltipOptions: {
    allowHTML: true,
    placement: "left",
    arrow: true,
    theme: "light",
    hideOnClick: true,
  },
  colors: {
    viridis: [
      "#fde725",
      "#b5de2b",
      "#6ece58",
      "#35b779",
      "#1f9e89",
      "#26828e",
      "#31688e",
      "#3e4989",
      "#482878",
      "#440154",
    ],
  },
}

const WordcloudComponent = (props) => {
  const [state, setState] = useState({ clicked: null, hovered: null })
  const width = props.args["width"] || initialSettings.width
  const height = props.args["height"] || initialSettings.height
  const fontScale = props.args["fontScale"] || initialSettings.fontScale
  const fontMin = parseInt(props.args["fontMin"])
  const fontMax = parseInt(props.args["fontMax"])
  const padding = parseInt(props.args["padding"]) || initialSettings.padding
  const mode = props.args["layout"] || initialSettings.spiral
  const scale = props.args["scaling"] || initialSettings.scale
  const enableTooltip =
    props.args["enableTooltip"] === undefined
      ? initialSettings.enableTooltip
      : props.args["enableTooltip"]
  const tooltipOptions =
    props.args["tooltipOptions"] || initialSettings.tooltipOptions
  const tooltipDataFields = props.args["tooltipDataFields"];
  const words = props.args['words']||[];
  const maxWords = props.args["maxWords"] || words.length
  const colors =
    props.args["paletteColors"] || initialSettings.colors["viridis"]
  const perWordColoring = props.args["perWordColoring"];
  // Initialize Options
  const options = {
    colors: colors,
    fontFamily: "roboto",
    fontSizes:
      fontMin && fontMax
        ? [fontMin, fontMax]
        : [
            parseInt(initialSettings.fontMin * fontScale),
            parseInt(initialSettings.fontMax * fontScale),
          ],
    padding: padding,
    rotations: 3,
    rotationAngles: [-90, 90],
    spiral: mode,
    scale: scale,
    transitionDuration: 500,
    // Non-configurable
    deterministic: true,
    enableOptimizations: true,
    enableTooltip: enableTooltip,
    tooltipOptions: tooltipOptions,
  }
  // Callback Handlers
  const onWordClicked = (word) => {
    setState((state) => {
      return {
        clicked: word,
        hovered: state.hovered,
      }
    });
  }
  const onWordHovered = (word) => {
    setState((state) => {
      return {
        clicked: state.clicked,
        hovered: word,
      }
    })
  }
  const getWordColor = (word) => word.color;
  const formatTooltipLayout = (word) => {
    let innerHTML = "";
    for (const property in tooltipDataFields) {
      innerHTML += `<span><b>${tooltipDataFields[property]}</b>: ${word[property]}</span></br>`
    }
    return innerHTML
  }

  const callbacks = {
    getWordColor: perWordColoring? getWordColor:undefined,
    onWordClick: (word) => onWordClicked(word),
    onWordMouseOver: (word) => onWordHovered(word),
    onWordMouseOut: (word) => onWordHovered(null),
    getWordTooltip: (word) => formatTooltipLayout(word),

  }
  // Return state to Streamlit
  useEffect(() => {
    Streamlit.setComponentValue(state);
  }, [state])
  useEffect(() => {
    Streamlit.setFrameHeight()
  })

  return (
    <div>
      <div style={{ width: width, height: height }}>
        <ReactWordCloud
          words={words}
          options={options}
          maxWords={maxWords}
          callbacks={callbacks}
        />
      </div>
    </div>
  )
}

export default withStreamlitConnection(WordcloudComponent)
