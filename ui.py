import streamlit as st
from orchestrator.orchestrator import run_orchestrator
from agents.parser_agent import parse_user_request

st.title("✈️ Travel AI System")

query = st.text_input("Enter travel request")

if st.button("Search"):
    parsed = parse_user_request(query)
    result = run_orchestrator(parsed)

    st.write(result)