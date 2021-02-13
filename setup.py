import setuptools

setuptools.setup(
    name="streamlit-wordcloud",
    version="0.1.0",
    author="Reza Hosseini",
    author_email="re1372@gmail.com",
    description="This is an interactive Wordcloud component for Streamlit. This is based on React-Wordcloud (https://github.com/chrisrzhou/react-wordcloud).",
    long_description="",
    long_description_content_type="text/plain",
    url="https://github.com/rezaho/streamlit-wordcloud",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.63",
        "numpy==1.20.0",
        "matplotlib==3.3.4",
    ],
)
