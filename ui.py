import streamlit as st
from agents.parser_agent import parse_user_request
from orchestrator.orchestrator import run_orchestrator

st.title("✈️ AI Travel Assistant (Production Mode)")

query = st.text_input("Enter trip (e.g. Paris to Tokyo)")

if st.button("Generate Plan"):

    parsed = parse_user_request(query)
    result = run_orchestrator(parsed)

    st.subheader("✈️ Flights")
    st.write(result["flights"])

    st.subheader("🏨 Hotels (Fallback Safe)")
    st.write(result["hotels"])

    st.subheader("🌦 Weather")
    st.write(result["weather"])