import streamlit as st
from graph import graph

st.set_page_config(page_title="Multi-Agent DSA Assistant", layout="wide")

st.title("Multi-Agent Coding Interview Assistant")
st.write("Paste a DSA problem and let multiple agents solve it step by step.")

with st.form("problem_form"):
    user_input = st.text_area("Enter your coding problem:", height=300)
    submit = st.form_submit_button("Run Assistant")


#3b 
if submit:
    if not user_input.strip():
        st.warning("Please enter a coding problem.")
    else:
        initial_state = {
            "problem": user_input,
            "topic": "",
            "bruteforce": "",
            "optimized": "",
            "code": "",
            "review": "",
            "explanation": "",
            "needs_fix": False,
            "retry_count": 0
        }
    with st.spinner("Agents are solving the problem..."):
        result = graph.invoke(initial_state)

        st.success("Analysis completed!")

        with st.expander("Detected Topic", expanded=True):
            st.write(result["topic"])

        with st.expander("Brute Force Approach"):
            st.write(result["bruteforce"])

        with st.expander("Optimized Approach"):
            st.write(result["optimized"])

        with st.expander("Final C++ Code"):
            st.code(result["code"], language="cpp")

        with st.expander("Review"):
            st.write(result["review"])

        with st.expander("Final Explanation"):
            st.write(result["explanation"])