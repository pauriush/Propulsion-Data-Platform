import streamlit as st

introduction = st.Page("documentation/introduction.py", title="Introduction", default=True)
features = st.Page("documentation/features.py", title="Features")
tutorial_1 = st.Page("tutorials/tutorial-1.py", title="Tutorial 1")
make_vs_buy = st.Page("resources/make-vs-buy.py", title="Make vs Buy")

pg = st.navigation(
    {
        "Documentation": [introduction, features],
        "Tutorials": [tutorial_1],
        "Resources": [make_vs_buy],
    }
)

pg.run()
