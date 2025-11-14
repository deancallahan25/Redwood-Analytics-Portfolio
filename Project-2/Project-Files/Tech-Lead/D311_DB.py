import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

#run the file py -m streamlit run d311_db.py
# or streamlit run d311_db.py

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
    st.header("Transportation Radius Map")

    # Coordinates for Cal Poly Humboldt
    lat, lon = 40.8758, -124.0786

    # Create Folium map
    m = folium.Map(location=[lat, lon], zoom_start=13)

    # Marker for the campus
    folium.Marker(
        [lat, lon],
        popup="Cal Poly Humboldt University",
        tooltip="Campus Center"
    ).add_to(m)

    # Define radius (in meters) for each transport method
    radius_map = {
        "WALK": 800,      # about 10 minutes walking distance
        "BIKE": 1000,     # short bike ride
        "SHUTTLE": 1700,  # local shuttle coverage
        "CAR": 3000      # drivable range from campus
    }

    color_map = {
        "WALK": "green",
        "BIKE": "orange",
        "SHUTTLE": "purple",
        "CAR": "blue"
    }

    # Add circles for each selected method
    for method in tickers:
        if method in radius_map:
            folium.Circle(
                location=[lat, lon],
                radius=radius_map[method],
                color=color_map.get(method, "gray"),
                fill=True,
                fill_opacity=0.3,
                popup=f"{method} radius: {radius_map[method]} m"
            ).add_to(m)

    # Display map
    st_folium(m, width=800, height=500)
    st.caption("Each circle shows the approximate travel radius from Cal Poly Humboldt by transport type.")

bottom_left_cell = cols[0].container(
    border=True, height="stretch", vertical_alignment="center"
)


st.subheader("Data Preview")
st.dataframe(df.head())
