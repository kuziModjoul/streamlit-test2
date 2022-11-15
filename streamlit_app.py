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

auth = False
## We have  to authenticate the user before they can view the contents of the webpage
while auth == False:

    col1, col2, col3 = st.columns((.5,1,.5))
    with col2:
        st.markdown("### Please Authenticate using the Username and Password you were provided")
        username = st.text_input("Username...")
        password = st.text_input("Password...")