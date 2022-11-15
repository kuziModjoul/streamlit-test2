import streamlit as st



st.set_page_config( page_title="Streamlit Test App",
                    page_icon= "random",
                    layout="wide"
 )

col1, col2, col3 = st.columns((.1,1,.1))

with col1:
    st.write("")

with col2:
    st.markdown(" <h1 style='text-align: center;'> This is an Example Streamlit with Authentication</h1>", unsafe_allow_html=True)

with col3:
    st.write("")

## We have  to authenticate the user before they can view the contents of the webpage

st.text_input("")