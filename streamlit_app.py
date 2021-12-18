import streamlit as st

st.title("IndicNLP!")

st.text("This is our Final Year Project,")
st.text("Implementing various features of NLP i.e,")
st.text("Natural Language Processing in Various Indic Languages.")
st.text("To Begin with Hindi,")
st.text("Here are Few Modules we have Implemented :-")

add_selectbox = st.sidebar.selectbox(
    "Which Module would you like to try?",
    ("Part-of-Speech Tagging", "Questiom & Answer", "Grammar Checking")
)

if add_selectbox == "Part-of-Speech Tagging" :
    st.header('Part-Of-Speech, PoS-Tagging :- ')
    pos_ip = st.text_input('Enter a Statement')
	pos_btn = st.button("Process")
	if pos_btn:
	    st.error("work's in progress :construction:, Come again later :smiley:")

if add_selectbox == "Questiom & Answer" :
	st.header('Question & Answering :- ')
	text = st.text_area("Text to analyze")
	que_ip = st.text_input('Enter the question')
	qna_btn = st.button("Answer")
	if qna_btn:
	    st.success("work's in progress :construction:, Come again later :smiley:")

if add_selectbox == "Grammar Checking" :
	st.header('Grammar Correction :- ')
	grm_ip = st.text_input('Enter the Statement')
	grm_btn = st.button("Check Grammar")
	if grm_btn:
	    st.write("work's in progress :construction:, Come again later :smiley:")

st.caption('Thank you for Tuning in, Come back for more :heart:')
