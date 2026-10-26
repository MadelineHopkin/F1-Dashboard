F1 TELEMETRY DASHBOARD 
A Python based telemetry analysis dashboard for Fomrula 1, build using Streamlit and FastF1.

The dashboard currently allows users to compare telemetry traces from real F1 sessions, providing insights into driver performance through speed, throttle, and break analysis.

FEATURES: 
- Compare telemetry data from two drivers 
- Speed trace visualisation
- Throttle trace visualisation
- Brake trace visualisation
- Year, race, session selection 
- Fastest lap analysis 
- Interactive dashboard (Streamlit)


SOFTWARE / TECHNOLOGIES USED
- Python 
- Streamlit 
- FastF1
- Pandas
- Matplotlib


EXAMPLE ANALYSIS 
Users can: 
- Select a season (year)
- Select a race weekend 
- Select a session 
- Compare two drivers fastest laps 

The dashboard can then visualise:
- Speed vs distance 
- Throttle vs distance 
- Brake vs distance

using telemetry data from FastF1.


INSTALLATION
Clone the repository 

# Navigate to the project directory 
cd F1-Telemetry-Dashboard

# Create and activate a virtual environment 
python -m venv venv

venv\Scripts\activate

# Install dependencies 
pip install -r requirements.txt

a free F1 account login may be required to access data from FastF1

# Run the dashboard
streamlit run app.py



FUTURE DEVELOPMENTS
- Add all races and seasons
- Delta time analysis 
- Sector performance comparison
- Tyre degredation analysis