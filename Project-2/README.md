## Project 2 README File

## Project 2 - Streamlit Dashboard Project - Should I Bring a Car to Campus
### Created by Redwood Analytics
- Tech Lead: Jaiden Roe - jaidenroe@gmail.com, Github: https://github.com/m0chii-choco
- Project Manager: Dean Callahan - deancallahan25@gmail.com - GitHub: https://github.com/deancallahan25
- Domain Expert: Zachary Griffiths - zgriffiths73@gmail.com, GitHub: https://github.com/WatermelonGOD7
- Quality Assurance: Evan Blem - blem3147@gmail.com, GitHub: https://github.com/bleme8779
- Streamlit cloud link: https://redwood-analytics-project2.streamlit.app/

### Setup Instruction: 
The Streamlit Dashboard is deployed to Streamlit Cloud and can be accessed here at this link https://redwood-analytics-project2.streamlit.app/. Once you have clicked the link, you will see a textbox where you can enter a Google API Key. If you enter a key, you will then be able to see dynamic commute time estimates based on where you click.  Otherwise, you will be unable to see this information. Additionally, if you provide an API key you will see two visualizaions describing the commute times and distances for each mode of transportion. It will also generate a custom recommendation message about whether you should bring a car to campus. 

### Dashboard Features:
-Toggle for bus stops: When the user enables this toggle, they will see the bus stops locations on the interactive map. Students at Cal Poly Humboldt have access to these bus routes for free through the Jack Pass program.
-Toggle for unit conversions: The user can change between kilometers and miles for the commute distance information.
-Custom recommendation based on user selection: When the user selects a point on the map, they will see commute time estimates from this location to campus. If any of the estimates are longer than our thresholds of a walking time greater than 20 minutes, a biking time greater than 30 minutes, or a transit time greater than 45 minutes, it will recommend you bring a car to campus. 
-Commute Visualizations: There are two different visualizations that appear representing the commute data. There is a bar chart for commute times and a bar chart for commute distances for each mode of transportation. The user can use these visualizations to aid in their decision to whether they should bring a car to campus. 

### Project Goals: 
We have created an interactive Streamlit Dashboard that students at Cal Poly Humboldt can use to make a data driven decision about whether they should bring a car to campus. Our project showcases our skills in group collaboration, GitHub practices, data cleaning, data visualizations, interacting with API's, using Quarto, and creating dashboards. Additionally, we followed proper data privacy practices with our protection of individual addresses. 

### Data Sources:
- population_addresses_2024_25_messy.csv: a simulated data set which contains messy student address data. It was cleaned and used in the app as the file "final_address_data.csv".
- simulated_commuter_survey_5yrs_messy.csv: a simulated data set which contains sample messy survey results describing transportion information from students, staff, and faculty. It was cleaned and used in the app as the file "lon_lat_final_data.csv".
-**Important note**: All of the above datasets are mock data which simulate actual student and survey data collected by Cal Poly Humboldt.
- jack-pass-bus-stops.csv: A dataset created by our Domain Expert which describes bus stops locations which students can use for free witht their Jack Pass. 

### Team Contributions:
- Jaiden Roe: Tech Lead for the project responsible for the coding of the streamlit dashboard and creation of the visualizations. 
- Zachary Griffith: Domain Expert for the project responsible for finding additional API's, ensuring dashboard was relevant to the domain, and that the dashboard was user-friendly. 
- Evan Blem: Quality Assurance for the project responsible for the data cleaning.
- Dean Callahan: Project Manager for the project responsible for the project planning, file coordination, project documentation, and structuring the GitHub repository. 

## Resources used: 
- Python Libraries: Streamlit, Pandas, Folium 
- API's: Google Maps API
- Additional Resources: Quarto, Public Transit Information (Jack Pass Bus Stops)



