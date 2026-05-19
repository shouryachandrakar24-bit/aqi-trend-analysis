# aqi-trend-analysis
A Python data analysis project fetching historical Air Quality Index (AQI) data via public APIs to visualize long-term pollution trends.
# Air Quality Index (AQI) Trend Analysis

## 📌 Project Overview
This project focuses on analyzing historical Air Quality Index (AQI) trends over time using Python. By leveraging the `requests` library to collect raw data from the Open-Meteo API and `pandas` for data processing, the script transforms raw particulate matter metrics (PM2.5 and PM10) into comprehensive time-series visualizations.

*(Note: This project fulfills the requirements for Project Allocation No. 10).*

## 🛠️ Tools & Technologies Used
* **Language:** Python
* **Data Collection:** API calls via the `requests` library (Open-Meteo Air Quality API)
* **Data Processing:** `pandas`
* **Data Visualization:** `matplotlib`

## 📊 Deliverables Included
1. **Time-Series Analysis:** A clean Pandas DataFrame structured with Datetime indexing.
2. **Trend Charts:** A plotted visualization comparing PM2.5 and PM10 concentrations over a multi-year period.
3. **Key Insights:** Automated identification of peak pollution months and cleanest air periods.

## 🚀 How to Run the Script
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/aqi-trend-analysis.git](https://github.com/YOUR_USERNAME/aqi-trend-analysis.git)

Install the required dependencies:

   pip install pandas requests matplotlib

Run the script:

python main.py
   
