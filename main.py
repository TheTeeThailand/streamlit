import streamlit as st

st.title("Getting Stared Streamlit")
st.write("test")


code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")


run_btn = st.button("Run!")
if run_btn:
    st.markdown("Button has already clicked")