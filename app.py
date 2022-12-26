import streamlit as st
import linear_regression
import index

Pages = {
    "Home": index,
    "1.Linear Regression": linear_regression
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(Pages.keys()))
page = Pages[selection]
page.app()
