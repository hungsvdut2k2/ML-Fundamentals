import streamlit as st
import linear_regression
import index
import logistic_regression

Pages = {
    "Home": index,
    "1.Linear Regression": linear_regression,
    "2.Logistic Regression": logistic_regression
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(Pages.keys()))
page = Pages[selection]
page.app()
