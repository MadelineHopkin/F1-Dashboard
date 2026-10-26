import streamlit as st
import fastf1
import matplotlib.pyplot as plt
import os 

#Enable FastF1 cache
fastf1.Cache.enable_cache("cache")

#Configure dashboard layout
st.set_page_config(
    page_title="F1 Dashboard",
    layout="wide"
)

st.title("F1 Dashboard")

st.subheader("Driver Telemetry Comparison")

st.sidebar.header("Session Selection")

year = st.sidebar.selectbox(
    "Year",
    [2021, 2022, 2023, 2024]
)

race = st.sidebar.selectbox(
    "Race",
    [
        "Bahrain Grand Prix",
        "Saudi Arabian Grand Prix",
        "Australian Grand Prix",
        "Monaco Grand Prix",
        "British Grand Prix",
        "Belgian Grand Prix",
        "Italian Grand Prix"
    ]
)

session_type = st.sidebar.selectbox(
    "Session",
    ["FP1", "FP2", "FP3", "Q", "R"]
)

# Load session
with st.spinner("Loading session..."):

    session = fastf1.get_session(
    year,
    race,
    session_type
)

    session.load(
        laps=True,
        telemetry=True,
        weather=False,
        messages=False
    )
st.write("Laps loaded:",
         hasattr(session, "_laps"))

#Get a list of drivers in the session
drivers = sorted(
    session.laps["Driver"].dropna().unique()    
)

col1, col2 = st.columns(2)

with col1:
    driver1 = st.selectbox(
        "Driver 1",
        drivers
    )

with col2:
    driver2 = st.selectbox(
        "Driver 2",
        drivers,
        index=1
    )

tab1, tab2, tab3 = st.tabs(
    [
        "Speed",
        "Throttle",
        "Brake"
    ]
)  

# Fastest laps
lap1 = (
    session.laps
    .pick_driver(driver1)
    .pick_fastest()
)

lap2 = (
    session.laps
    .pick_driver(driver2)
    .pick_fastest()
)

# Telemetry
tel1 = lap1.get_car_data().add_distance()
tel2 = lap2.get_car_data().add_distance()

# Metrics
st.subheader("Fastest Laps")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        driver1,
        str(lap1["LapTime"])
    )

with col2:
    st.metric(
        driver2,
        str(lap2["LapTime"])
    )

# Top Speeds

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Top Speed",
        f"{tel1['Speed'].max():.1f} km/h"
    )

with col2:
    st.metric(
        "Top Speed",
        f"{tel2['Speed'].max():.1f} km/h"
    )


# Speed Telemetry Commparison
with tab1:

    fig, ax = plt.subplots(figsize=(12,6))

    ax.plot(
        tel1["Distance"],
        tel1["Speed"],
        label=driver1
    )

    ax.plot(
        tel2["Distance"],
        tel2["Speed"],
        label=driver2
    )

    ax.set_title("Speed Comparison")
    ax.set_xlabel("Distance (m)")
    ax.set_ylabel("Speed (km/h)")
    ax.grid(True)
    ax.legend()

    st.pyplot(fig)

# Throttle Telemetry Comparison
with tab2:

    fig, ax = plt.subplots(figsize=(12,6))

    ax.plot(
        tel1["Distance"],
        tel1["Throttle"],
        label=driver1
    )

    ax.plot(
        tel2["Distance"],
        tel2["Throttle"],
        label=driver2
    )

    ax.set_title("Throttle Comparison")
    ax.set_xlabel("Distance (m)")
    ax.set_ylabel("Throttle (%)")
    ax.grid(True)
    ax.legend()

    st.pyplot(fig)

# Brake Telemetry Comparison
with tab3:

    fig, ax = plt.subplots(figsize=(12,6))

    ax.plot(
        tel1["Distance"],
        tel1["Brake"].astype(int) * 100,
        label=driver1
    )

    ax.plot(
        tel2["Distance"],
        tel2["Brake"].astype(int) * 100,
        label=driver2
    )

    ax.set_title("Brake Comparison")
    ax.set_xlabel("Distance (m)")
    ax.set_ylabel("Brake (%)")
    ax.grid(True)
    ax.legend()

    st.pyplot(fig)   