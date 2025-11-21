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
    df = pd.read_csv("Project-2/streamlit_app/data/final_address_data.csv")
    return df

df = load_data()

def load_data_two():
    df = pd.read_csv("Project-2/streamlit_app/data/jack-pass-bus-stops.csv")
    return df

df_two = load_data_two()

#load the validated lon lat data from the suvery data file
def load_data_three():
    df = pd.read_csv("Project-2/streamlit_app/data/lon_lat_final_data.csv")
    return df
df_three = load_data_three()

st.header("Google Maps API (Optional)")

api_key_test = st.text_input(
        "Google Maps API Key",
        type = "password",
        help = "Optional: enable Directions API in Google Cloud Console"
    )

st.header("Toggle Information")
bus_stops_on = st.toggle("Show bus stops")
if bus_stops_on:
    st.write("Bus stops are displayed on the map.")
km_mode_on = st.toggle("Show distances in kilometers")
if km_mode_on:
    st.write("Distances are shown in kilometers.")

# PREPROCESS LIVING LOCATION CLUSTERS
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

    # Bus stops
    if bus_stops_on:
        for _, row in df_two.iterrows():
            folium.CircleMarker(
                [row['latitude'], row['longitude']],
                radius=3,
                popup=f"Stop ID: {row['stop_name']}",
                color='green',
                fill=True,
                fill_opacity=0.7,
                tooltip=f"Stop ID: {row['stop_name']}"
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

    for point in df_three.iterrows():
        folium.CircleMarker(
            [point['lat'], point['lon']],
            radius=3,
            color='orange',
            fill=True,
            fill_opacity=0.5,
            tooltip=f"Intersection Point"
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
                if km_mode_on:
                    st.markdown(f"<p style='font-size:20px;'><b>{label}:</b> {minutes:.1f} min • {km:.2f} km</p>", unsafe_allow_html=True)
                else: 
                    miles = km * 0.621371
                    st.markdown(f"<p style='font-size:20px;'><b>{label}:</b> {minutes:.1f} min • {miles:.2f} mi</p>", unsafe_allow_html=True)
        # DRIVING
        t, d = get_route(clicked_lat, clicked_lon, CAMPUS_LAT, CAMPUS_LON, "driving")
        show_route("Driving", t, d)
        if km_mode_on:
            commute_data.append({"Mode": "Driving", "Minutes": t, "Distance_km": d})
        else:
            commute_data.append({"Mode": "Driving", "Minutes": t, "Distance_mi": d*.621371})
        # Walking
        t, d = get_route(clicked_lat, clicked_lon, CAMPUS_LAT, CAMPUS_LON, "walking")
        show_route("Walking", t, d)
        if km_mode_on:
            commute_data.append({"Mode": "Walking", "Minutes": t, "Distance_km": d})
        else:
            commute_data.append({"Mode": "Walking", "Minutes": t, "Distance_mi": d*.621371})
        # Biking
        t, d = get_route(clicked_lat, clicked_lon, CAMPUS_LAT, CAMPUS_LON, "bicycling")
        show_route("Biking", t, d)
        if km_mode_on:
            commute_data.append({"Mode": "Biking", "Minutes": t, "Distance_km": d})
        else:
            commute_data.append({"Mode": "Biking", "Minutes": t, "Distance_mi": d*.621371})            
        # Transit
        t, d = get_route(clicked_lat, clicked_lon, CAMPUS_LAT, CAMPUS_LON, "Transit")
        show_route("Transit", t, d)
        if km_mode_on:
            commute_data.append({"Mode": "Transit", "Minutes": t, "Distance_km": d})
        else:
            commute_data.append({"Mode": "Transit", "Minutes": t, "Distance_mi": d*.621371})
    else:
        st.markdown("<p style='font-size:20px;'>Click a point on the map to estimate commute times.</p>", unsafe_allow_html=True)
        
        commute_data = []


# ADD BAR CHART
if commute_data:
    df_commute = pd.DataFrame(commute_data)

    # --- MINUTES CHART ---
    df_minutes = df_commute[["Mode", "Minutes"]].copy()

    chart_minutes = (
        alt.Chart(df_minutes)
        .mark_bar(color = "#1f77b4")  # Blue
        .encode(
            x = alt.X("Mode:N", title = "Transportation Mode"),
            y = alt.Y("Minutes:Q", title = "Minutes"),
            tooltip = ["Mode", "Minutes"]
        )
        .properties(title = "Commute Time (Minutes)", width = 300, height = 300)
    )

    # --- DISTANCE CHART ---
    df_distance = df_commute[["Mode", "Distance_mi"]].copy()

    chart_distance = (
        alt.Chart(df_distance)
        .mark_bar(color = "#2ca02c")  # Green
        .encode(
            x = alt.X("Mode:N", title = "Transportation Mode"),
            y = alt.Y("Distance_mi:Q", title = "Distance (mi)"),
            tooltip = ["Mode", "Distance_mi"]
        )
        .properties(title="Commute Distance (mi)", width=300, height=300)
    )

    st.header("Commute Time & Distance")
    col1, col2 = st.columns(2)
    with col1:
        st.altair_chart(chart_minutes)
    with col2:
        st.altair_chart(chart_distance)


# Recommendation Logic

def get_minutes_for_mode(mode):
    for row in commute_data:
        if row['Mode'] == mode:
            return row['Minutes']
    return None

drive_time=get_minutes_for_mode("Driving")
walk_time=get_minutes_for_mode("Walking")
biking_time=get_minutes_for_mode("Biking")
transit_time=get_minutes_for_mode("Transit")


#can change these values possibly based on user input later
bring_car = None
max_walk_time=20 
max_bike_time=30 
max_transit_time=45  

if(walk_time!=None):
    if(walk_time > max_walk_time):
        bring_car=True
    else:
        bring_car=False
elif(biking_time!=None):
    if(biking_time > max_bike_time):
        bring_car=True
    else:
        bring_car=False
elif(transit_time!=None):
    if(transit_time > max_transit_time):
        bring_car=True
    else:
        bring_car=False


# Recommendation Text

st.header("Recommendation")
if bring_car==True:
    st.success("We recommend bringing a car to campus")
elif bring_car==False:
    st.text("We do not recommend bringing a car to campus")
else:
    st.text("No recommendation available at this time")



