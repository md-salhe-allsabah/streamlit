import streamlit as st

st.set_page_config(
    page_title="Allsabah's app",
    page_icon='😅'
)

st.title('Hello World')
st.divider()

with st.container(border=True):
    st.write(
        "Hi, I'm allsabah, Hopefully this streamlit app is hosted successfully on the streamlit cloud. I'm intended to dump here some of my important and frequently used resource links as my college and university's sites get crashed every alternate week."
    )

st.divider()

st.subheader("JUT Ranchi BTech Syllabus")

import pandas as pd

from url import urls

st.dataframe(
    pd.DataFrame(urls.items(), columns=["Years", "Link"]),
    column_config={"Link": st.column_config.LinkColumn("Google Drive Link")},
    hide_index=True,
)