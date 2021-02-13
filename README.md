# Streamlit WordCloud Component

This is a Streamlit wrapper For [React Wordcloud](https://github.com/chrisrzhou/react-wordcloud) with some minor modifications.


## Overview

You can use this Streamlit component to create beautiful and interactive WordCloud visualization as shown in the image below. 

![WordCloud Example](./img/wordcloud-example.png)

## Quickstart

* Clone this repo.
1. Create a new Python virtual environment for the package to be install (Optional):
```
$ python3 -m venv .venv  # create venv
$ .venv/bin/activate   # activate venv
```
2. Install the package from PyPi
```
$ pip install streamlit-wordcloud # install streamlit wordcloud package
```
* Run example provided in `usage-example.py`:
```
$ streamlit run usage-example.py
```
* Open `` in your browser.
* If everything goes well you should be able to see a page similar to this:
![Usage Example](./img/usage-example.png)

## Examples

```python
import streamlit as st 
import streamlit_wordcloud as wordcloud

words = [
    dict(text="Robinhood", value=16000, color="#b5de2b", country="US", industry="Cryptocurrency"),
    dict(text="Personio", value=8500, color="#b5de2b", country="DE", industry="Human Resources"),
    dict(text="Boohoo", value=6700, color="#b5de2b", country="UK", industry="Beauty"),
    dict(text="Deliveroo", value=13400, color="#b5de2b", country="UK", industry="Delivery"),
    dict(text="SumUp", value=8300, color="#b5de2b", country="UK", industry="Credit Cards"),
    dict(text="CureVac", value=12400, color="#b5de2b", country="DE", industry="BioPharma"),
    dict(text="Deezer", value=10300, color="#b5de2b", country="FR", industry="Music Streaming"),
    dict(text="Eurazeo", value=31, color="#b5de2b", country="FR", industry="Asset Management"),
    dict(text="Drift", value=6000, color="#b5de2b", country="US", industry="Marketing Automation"),
    dict(text="Twitch", value=4500, color="#b5de2b", country="US", industry="Social Media"),
    dict(text="Plaid", value=5600, color="#b5de2b", country="US", industry="FinTech"),
]
return_obj = wordcloud.visualize(words, tooltip_data_fields={
    'text':'Company', 'value':'Mentions', 'country':'Country of Origin', 'industry':'Industry'
}, per_word_coloring=False)
```

## Development

* Ensure you have [Python 3.6+](https://www.python.org/downloads/), [Node.js](https://nodejs.org), and [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) installed.
* Clone this repo.
* Create a new Python virtual environment for the template:
```
$ python3 -m venv .venv  # create venv
$ .venv/bin/activate   # activate venv
$ pip install streamlit # install streamlit
```
* Initialize and run the component template frontend:
```
$ cd stream_wordcloud/frontend
$ npm install    # Install npm dependencies
$ npm run start  # Start the Webpack dev server
```
* From a separate terminal, run the template's Streamlit app:
First open `stream_wordcloud/streamlit_wordcloud.py` in an editor of your choice and change `_RELEASE` to `False`.
```
$ .venv/bin/activate  # activate the venv you created earlier
$ streamlit run stream_wordcloud/streamlit_wordcloud.py  # run the example
```