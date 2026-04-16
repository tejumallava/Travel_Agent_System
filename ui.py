import streamlit as st
from agents.parser_agent import parse_user_request
from orchestrator.orchestrator import run_orchestrator

st.title("✈️ AI Travel Agent System")

query = st.text_input("Enter travel request (e.g. Paris to Atlanta next week)")

if st.button("Search"):

    parsed = parse_user_request(query)
    result = run_orchestrator(parsed)

    st.subheader("Flights")
    st.json(result["flights"])

    st.subheader("Hotels")
    st.json(result["hotels"])

    st.subheader("Weather")
    st.json(result["weather"])