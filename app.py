import streamlit as st

st.set_page_config(page_title="Travel AI", layout="centered")

st.title("✈️ AI Travel Planner")

# ---------------- INPUT FORM ----------------
origin = st.text_input("Origin City (e.g. Paris)")
destination = st.text_input("Destination City (e.g. Atlanta)")
date = st.date_input("Travel Date")

# ---------------- MOCK RESULTS ----------------
def get_flights(origin, destination, date):
    return [
        {"airline": "Delta", "price": "$450", "duration": "9h 30m"},
        {"airline": "Air France", "price": "$520", "duration": "9h 10m"},
    ]

def get_hotels(destination):
    return [
        {"name": "Hilton Downtown", "price": "$180/night"},
        {"name": "Marriott City Center", "price": "$210/night"},
    ]

# ---------------- SEARCH BUTTON ----------------
if st.button("Search Travel Options"):

    if not origin or not destination:
        st.error("Please enter both origin and destination")
    else:
        st.subheader("✈️ Flights")

        flights = get_flights(origin, destination, date)
        for f in flights:
            st.write(f"**{f['airline']}** | {f['price']} | {f['duration']}")

        st.subheader("🏨 Hotels")

        hotels = get_hotels(destination)
        for h in hotels:
            st.write(f"**{h['name']}** | {h['price']}")