import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import requests
import altair as alt



# CONFIGURATION
st.set_page_config(page_title="Transportation & Housing Dashboard", layout="wide")
st.title("🚗 Should I Bring a Car to Campus?")

CAMPUS_LAT = 40.8762
CAMPUS_LON = -124.0786

# 🔐 HARD-CODED GOOGLE MAPS API KEY (replace with your real key)
API_KEY = "AIzaSyCK28ITsrC4lM6QbGgm5NbrpJdHpytTUWE"


# DATA LOADING
@st.cache_data
def load_data():
    df = pd.read_csv("population_addresses_validated_test_100.csv")
    return df

df = load_data()


# PREPROCESS LIVING LOCATION CLUSTERS
@st.cache_data
def get_common_locations(df):
    valid = df[
        (df['current_geocode_status'] == 'ok') &
        df['current_lat'].notna() &
        df['current_lon'].notna()
    ].copy()

    valid['lat_r'] = valid['current_lat'].round(2)
    valid['lon_r'] = valid['current_lon'].round(2)

    groups = valid.groupby(['lat_r', 'lon_r']).agg({
        'current_lat': 'first',
        'current_lon': 'first',
        'current_city': 'first',
        'pop_id': 'count'
    }).reset_index()

    groups.columns = ['lat_r', 'lon_r', 'lat', 'lon', 'city', 'count']
    return groups.to_dict("records")

locations = get_common_locations(df)


# MAP + ROUTE CELLS
st.header("Transportation Map")

left, right = st.columns([1.3, 1])  # slightly wider map, narrower right cell

# LEFT CELL → MAP
with left:
    m = folium.Map(location=[CAMPUS_LAT, CAMPUS_LON], zoom_start=13)

    # Campus marker
    folium.Marker(
        [CAMPUS_LAT, CAMPUS_LON],
        popup="Cal Poly Humboldt",
        tooltip="Campus Center",
        icon=folium.Icon(color="red", icon="university", prefix="fa")
    ).add_to(m)

    # Housing clusters
    for loc in locations:
        folium.CircleMarker(
            [loc['lat'], loc['lon']],
            radius=loc['count'] / 2,
            popup=f"{loc['city']}<br>Students: {loc['count']}",
            color='blue',
            fill=True,
            fill_opacity=0.6,
            tooltip=f"{loc['city']} ({loc['count']} students)"
        ).add_to(m)

    map_data = st_folium(m, width=900, height=600, returned_objects=["last_clicked"])
    clicked = map_data.get("last_clicked")


# RIGHT CELL → ROUTE ESTIMATES
with right:
    if clicked:
        clicked_lat = clicked["lat"]
        clicked_lon = clicked["lng"]

        st.markdown("<h2>Commuting Times</h2>", unsafe_allow_html=True)

        # nearest city cluster
        closest = min(
            locations,
            key=lambda loc: (loc["lat"] - clicked_lat)**2 + (loc["lon"] - clicked_lon)**2
        )

        st.markdown(f"<p style='font-size:20px;'><b>Closest:</b> {closest['city']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size:20px; margin-bottom:10px;'><b>Students:</b> {closest['count']}</p>", unsafe_allow_html=True)

        commute_data = []  # store data for bar chart

        # GOOGLE DIRECTIONS API FUNCTION
        def get_route(start_lat, start_lon, end_lat, end_lon, mode):
            url = "https://maps.googleapis.com/maps/api/directions/json"
            params = {
                "origin": f"{start_lat},{start_lon}",
                "destination": f"{end_lat},{end_lon}",
                "mode": mode,
                "key": API_KEY
            }
            response = requests.get(url, params=params)
            data = response.json()
            if data["status"] != "OK":
                return None, None
            leg = data["routes"][0]["legs"][0]
            return leg["duration"]["value"]/60, leg["distance"]["value"]/1000


        # SHOW ROUTE FUNCTION (BIGGER TEXT)
        def show_route(label, minutes, km):
            if minutes is None or km is None:
                st.markdown(f"<p style='font-size:20px;'><b>{label}:</b> not available</p>", unsafe_allow_html=True)
            else:
                st.markdown(f"<p style='font-size:20px;'><b>{label}:</b> {minutes:.1f} min • {km:.2f} km</p>", unsafe_allow_html=True)
        # DRIVING
        t, d = get_route(clicked_lat, clicked_lon, CAMPUS_LAT, CAMPUS_LON, "driving")
        show_route("Driving", t, d)
        commute_data.append({"Mode": "Driving", "Minutes": t, "Distance_km": d})

        # Walking
        t, d = get_route(clicked_lat, clicked_lon, CAMPUS_LAT, CAMPUS_LON, "walking")
        show_route("Walking", t, d)
        commute_data.append({"Mode": "Walking", "Minutes": t, "Distance_km": d})

        # Biking
        t, d = get_route(clicked_lat, clicked_lon, CAMPUS_LAT, CAMPUS_LON, "bicycling")
        show_route("Biking", t, d)
        commute_data.append({"Mode": "Biking", "Minutes": t, "Distance_km": d})

        # Transit
        t, d = get_route(clicked_lat, clicked_lon, CAMPUS_LAT, CAMPUS_LON, "transit")
        show_route("Transit", t, d)
        commute_data.append({"Mode": "Transit", "Minutes": t, "Distance_km": d})

    else:
        st.markdown("<p style='font-size:20px;'>Click a point on the map to estimate commute times.</p>", unsafe_allow_html=True)
        commute_data = []


# ADD BAR CHART
if commute_data:
    df_commute = pd.DataFrame(commute_data)
    
    # Melt dataframe for Altair plotting
    df_melt = df_commute.melt(id_vars="Mode", value_vars=["Minutes", "Distance_km"],
                              var_name="Type", value_name="Value")

    chart = alt.Chart(df_melt).mark_bar().encode(
        x=alt.X("Mode:N", title="Transportation Mode"),
        y=alt.Y("Value:Q", title="Value"),
        color="Type:N",
        tooltip=["Mode", "Type", "Value"]
    ).properties(width=300, height=300)

    st.header("Commuting Times & Distances")
    st.altair_chart(chart)


# RAW DATA PREVIEW
st.header("Raw Data Preview")
st.dataframe(df.head())
