import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# --- Streamlit setup ---
st.set_page_config(
    page_title="Should I Bring a Car to Campus?",
    layout="wide"
)

st.title("🚗 Should I Bring a Car to Campus?")

cols = st.columns([1, 3])

METHODS = ["CAR", "WALK", "SHUTTLE", "BIKE"]
DEFAULT_METHODS = ["CAR", "WALK"]

def methods_str(methods):
    return ",".join(methods)

if "tickers_input" not in st.session_state:
    st.session_state.tickers_input = st.query_params.get(
        "methods", methods_str(DEFAULT_METHODS)
    ).split(",")

def update_query_param():
    if st.session_state.tickers_input:
        st.query_params["methods"] = methods_str(st.session_state.tickers_input)
    else:
        st.query_params.pop("methods", None)

# --- Sidebar or left cell input ---
top_left_cell = cols[0].container(
    border=True, height="stretch", vertical_alignment="center"
)

with top_left_cell:
    tickers = st.multiselect(
        "Transportation methods",
        options=sorted(set(METHODS)),
        default=st.session_state.tickers_input,
        placeholder="Choose transportation to compare. Example: BIKE",
        accept_new_options=True,
    )

tickers = [t.upper() for t in tickers]

if tickers:
    st.query_params["methods"] = methods_str(tickers)
else:
    st.query_params.pop("methods", None)

if not tickers:
    top_left_cell.info("Pick some transportation methods to compare", icon=":material/info:")
    st.stop()

# --- Load data ---
def load_data():
    df = pd.read_csv("population_addresses_validated_test_100.csv")
    return df

df = load_data()
st.success(f"Loaded {len(df)} student addresses")

# --- Right panel (visualization) ---
right_cell = cols[1].container(border=True, height="stretch", vertical_alignment="center")

# Right cell with the map
with right_cell:
    st.header("Interactive Map")

    # Create a Folium map centered at SF
    m = folium.Map(location=[40.8758, -124.0786], zoom_start=12)
    folium.Marker(
        [40.8758, -124.0786],
        popup="Cal Poly Humboldt University",
        tooltip="Click me"
    ).add_to(m)

    # Display the map
    st_folium(m, width=800, height=500)
    st.caption("Map showing student addresses and transportation options.")
