import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import requests

# PAGE SETTINGS
st.set_page_config(page_title="Transportation & Housing Dashboard", layout="wide")
st.title("🚗 Should I Bring a Car to Campus?")

CAMPUS_LAT = 40.8762
CAMPUS_LON = -124.0786

# DATA LOADING

@st.cache_data
def load_data():
    df= pd.read_csv("Project-2/streamlit_app/data/final_address_data.csv")
    return df
df= load_data_two()

# SIDEBAR CONTROLS

cols = st.columns([1, 3])

with cols[0]:
    st.header("Transportation Options")

    METHODS = ["CAR", "WALK", "SHUTTLE", "BIKE"]
    DEFAULT = ["CAR", "WALK"]

    tickers = st.multiselect(
        "Transportation methods",
        options = METHODS,
        default = DEFAULT,
        placeholder = "Choose transport methods",
    )

    tickers = [t.upper() for t in tickers]

    if not tickers:
        st.info("Pick at least one transportation method.")
        st.stop()

    st.divider()
    st.header("Google Maps API (Optional)")

    api_key = st.text_input(
        "Google Maps API Key",
        type = "password",
        help = "Optional: enable Directions API in Google Cloud Console"
    )



# COMPUTE COMMON LIVING LOCATIONS

@st.cache_data
def get_common_locations(df):
    valid = df[
        df['lat'].notna() &
        df['lon'].notna()
    ].copy()

    valid['lat_r'] = valid['lat'].round(2)
    valid['lon_r'] = valid['lon'].round(2)

    groups = valid.groupby(['lat_r', 'lon_r']).agg({
        'lat': 'first',
        'lon': 'first',
        'current_city': 'first',
        'pop_id': 'count'
    }).reset_index()

    groups.columns = ['lat_r', 'lon_r', 'lat', 'lon', 'city', 'count']

    return groups.to_dict("records")

locations = get_common_locations(df)

# ONE UNIFIED MAP (RADIUS + CLUSTERS + CLICK)

with cols[1]:
    st.header("Transportation Map")

    # BASE MAP
    m = folium.Map(location=[CAMPUS_LAT, CAMPUS_LON], zoom_start=13)

    # Campus marker
    folium.Marker(
        [CAMPUS_LAT, CAMPUS_LON],
        popup="Cal Poly Humboldt",
        tooltip="Campus Center",
        icon=folium.Icon(color="red", icon="university", prefix="fa")
    ).add_to(m)

    # Transport radii
    radius_map = {
        "WALK": 800,
        "BIKE": 1000,
        "SHUTTLE": 1700,
        "CAR": 3000
    }
    color_map = {
        "WALK": "green",
        "BIKE": "orange",
        "SHUTTLE": "purple",
        "CAR": "blue",
    }

    for method in tickers:
        folium.Circle(
            location = [CAMPUS_LAT, CAMPUS_LON],
            radius = radius_map.get(method, 0),
            color = color_map.get(method, "gray"),
            fill = True,
            fill_opacity = 0.25,
            popup = f"{method} radius"
        ).add_to(m)

    # Adding hosuing clusters with knn & with click interaction if the api is provided

    if api_key:
        st.success("API key detected — showing housing clusters & interactive routing.")

        # Add student living clusters
        for loc in locations:
            folium.CircleMarker(
                [loc['lat'], loc['lon']],
                radius = loc['count'] / 2,
                popup = f"{loc['city']}<br>Students: {loc['count']}",
                color = 'blue',
                fill = True,
                fill_opacity = 0.6,
                tooltip = f"{loc['city']} ({loc['count']} students)"
            ).add_to(m)

        # Map supports clicking
        map_data = st_folium(m, width=900, height=600, returned_objects=["last_clicked"])
    else:
        st.info("Enter a Google Maps API key to enable interactive commuting estimates.")
        # Static rendering — no clicks returned
        map_data = st_folium(m, width=900, height=600)

# Extract click only when allowed
clicked = map_data.get("last_clicked") if api_key else None

# Communting time / Distance estimates time of arrival

if clicked:
    clicked_lat = clicked["lat"]
    clicked_lon = clicked["lng"]

    st.subheader(
        f"Commuting Times from Selected Location ({clicked_lat:.4f}, {clicked_lon:.4f})"
    )

    # Find closest city grouping
    closest = min(
        locations,
        key = lambda loc: (loc["lat"] - clicked_lat)**2 + (loc["lon"] - clicked_lon)**2
    )

    st.write(f"Closest location: **{closest['city']}**")
    st.write(f"Student count: {closest['count']}")

    col1, col2, col3 = st.columns(3)

    #Google Api map
    if api_key:

        def get_route(start_lat, start_lon, end_lat, end_lon, mode):
            url = "https://maps.googleapis.com/maps/api/directions/json"
            params = {
                "origin": f"{start_lat},{start_lon}",
                "destination": f"{end_lat},{end_lon}",
                "mode": mode,
                "key": api_key
            }
            response = requests.get(url, params=params)
            data = response.json()
            if data["status"] != "OK":
                return None, None
            leg = data["routes"][0]["legs"][0]
            return leg["duration"]["value"]/60, leg["distance"]["value"]/1000  # minutes, km

        with col1:
            st.write("Walking")
            t, d = get_route(clicked_lat, clicked_lon, CAMPUS_LAT, CAMPUS_LON, "walking")
            st.metric("Time", f"{t:.1f} min")
            st.metric("Distance", f"{d:.2f} km")



        with col2:
            st.write("Biking")
            t, d = get_route(clicked_lat, clicked_lon, CAMPUS_LAT, CAMPUS_LON, "bicycling")
            st.metric("Time", f"{t:.1f} min")
            st.metric("Distance", f"{d:.2f} km")

        with col3:
            st.write("Transit")
            t, d = get_route(clicked_lat, clicked_lon, CAMPUS_LAT, CAMPUS_LON, "transit")
            st.metric("Time", f"{t:.1f} min")
            st.metric("Distance", f"{d:.2f} km")

    #Estimated (NO API KEY) 
    else:
        st.info("Enter a Google Maps API key for real travel times. Showing estimates instead.")

        dist_km = ((clicked_lat - CAMPUS_LAT)**2 + (clicked_lon - CAMPUS_LON)**2)**0.5 * 111

        with col1:
            st.write("Walking")
            st.metric("Time", f"{dist_km * 12:.1f} min")
            st.metric("Distance", f"{dist_km:.2f} km")

        with col2:
            st.write("Biking")
            st.metric("Time", f"{dist_km * 4:.1f} min")
            st.metric("Distance", f"{dist_km:.2f} km")

        with col3:
            st.write("Transit")
            st.metric("Time", f"{dist_km * 3:.1f} min")
            st.metric("Distance", f"{dist_km:.2f} km")



# Data Preview
st.header("Raw Data Preview")
st.dataframe(df.head())