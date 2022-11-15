import streamlit as st
import pandas as pd



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



def check_password():
    """Returns `True` if the user had a correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 User not known or password incorrect")
        return False
    else:
        # Password correct.
        return True
logged_in  =  False
with st.sidebar:

    if check_password():
        logged_in  =  True
        st.write("You're Logged in now!!! You can close the sidebar")

if logged_in:
        df = pd.read_csv("dir/file.csv")

        @st.experimental_memo
        def convert_df(df):
            return df.to_csv(index=False).encode('utf-8')


        csv = convert_df(df)

        st.download_button(
        "Press to Download",
        csv,
        "file.csv",
        "text/csv",
        key='download-csv'
        )