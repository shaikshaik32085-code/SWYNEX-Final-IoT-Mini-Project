SWYNEX Final IoT Mini-Project

Project Overview

This project simulates an IoT monitoring system using Python. It generates temperature and humidity readings, displays sensor data in a chart, and identifies high-temperature alerts.

Features

- Simulated temperature and humidity data
- Sensor readings saved in a CSV file
- Dashboard chart created using Matplotlib
- Alert when temperature exceeds 35°C

Alert Rule

Threshold: Temperature > 35°C

When the simulated temperature exceeds 35°C, the program displays a high-temperature alert.

Technologies Used

- Python
- Matplotlib
- CSV
- Random data simulation

How to Run

1. Install Matplotlib using "python -m pip install matplotlib".
2. Run "python iot_project.py".
3. View the generated dashboard chart and "sensor_data.csv" file.

Limitations

- Sensor values are simulated, not collected from physical hardware.
- The alert is displayed in the terminal; it does not send real notifications.
- The dashboard uses sample data rather than live IoT readings.

Conclusion

This project demonstrates basic IoT data simulation, visualization, and threshold-based alert logic.