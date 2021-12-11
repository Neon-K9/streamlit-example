import streamlit as st

"""
# IndicNLP!

This is our Final Year Project,
Implementing various features of NLP i.e,
Natural Language Processing in Various Indic Languages.
To Begin with Hindi.
Here are Few Modules we have Implemented :-

"""


with st.echo(code_location='below'):
    st.title("IndicNLP")
    
    st.header('Part-Of-Speech, PoS-Tagging :- ')
    pos_ip = st.text_input('Enter a Statement')
    pos_btn = st.button("Process")
    if pos_btn:
        st.error("work's in progress :construction:, Come again later :smiley:")
    
    st.header('Question & Answering :- ')
    text = st.text_area("Text to analyze")
    que_ip = st.text_input('Enter the question')
    qna_btn = st.button("Process")
    if qna_btn:
        st.success("work's in progress :construction:, Come again later :smiley:")
    
    st.header('Grammar Correction :- ')
    grm_ip = st.text_input('Enter a Statement')
    grm_btn = st.button("Process")
    if grm_btn:
        st.write("work's in progress :construction:, Come again later :smiley:")
    
    st.caption('Thank you for Tuning in, Come back for more :heart:')
    
