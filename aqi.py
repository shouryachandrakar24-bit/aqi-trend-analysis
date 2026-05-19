import pandas as pd
import requests
import matplotlib.pyplot as plt

print("Fetching AQI data via API...")
url = "https://air-quality-api.open-meteo.com/v1/air-quality"

params = {
    "latitude": 28.6139, 
    "longitude": 77.2090,
    "start_date": "2023-01-01",
    "end_date": "2025-12-31",
    "hourly": "pm10,pm2_5" 
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print("Data successfully fetched!")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    exit()

print("Processing data into a DataFrame...")
df = pd.DataFrame(data['hourly'])

df['time'] = pd.to_datetime(df['time'])

df.set_index('time', inplace=True)

monthly_trends = df.resample('ME').mean()

print("Generating trend charts...")
plt.figure(figsize=(12, 6))

plt.plot(monthly_trends.index, monthly_trends['pm2_5'], 
         label='PM 2.5 (Fine Particles)', color='crimson', linewidth=2, marker='o')

plt.plot(monthly_trends.index, monthly_trends['pm10'], 
         label='PM 10 (Coarse Particles)', color='steelblue', linewidth=2, marker='s')

plt.title('Monthly AQI Trends Over Time in New Delhi (2023-2025)', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Concentration (µg/m³)', fontsize=12)
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

print("\n--- Key Insights ---")
max_pm25_month = monthly_trends['pm2_5'].idxmax().strftime('%B %Y')
min_pm25_month = monthly_trends['pm2_5'].idxmin().strftime('%B %Y')

print(f"1. Peak Pollution: The highest average PM 2.5 levels occurred in {max_pm25_month}.")
print(f"2. Cleanest Air: The lowest average PM 2.5 levels were observed in {min_pm25_month}.")
print("3. Seasonal Trend: Particulate matter typically dips during monsoon/summer months and spikes dramatically during the winter due to temperature inversions.")
