import random
import csv
import matplotlib.pyplot as plt

# SWYNEX Final IoT Mini-Project

temperature = [round(random.uniform(22, 40), 1) for _ in range(10)]
humidity = [round(random.uniform(35, 80), 1) for _ in range(10)]
readings = list(range(1, 11))

threshold = 35

print("===== SWYNEX IoT MONITORING SYSTEM =====")

with open("sensor_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Reading", "Temperature_C", "Humidity_Percent"])

    for i in range(10):
        writer.writerow([readings[i], temperature[i], humidity[i]])

        print(
            f"Reading {i + 1}: "
            f"Temperature = {temperature[i]}°C, "
            f"Humidity = {humidity[i]}%"
        )

        if temperature[i] > threshold:
            print("  ALERT: High temperature!")

# Create dashboard chart
plt.figure(figsize=(10, 5))
plt.plot(readings, temperature, marker="o", label="Temperature (°C)")
plt.plot(readings, humidity, marker="s", label="Humidity (%)")
plt.axhline(
    y=threshold,
    linestyle="--",
    label="Alert Threshold (35°C)"
)

plt.title("SWYNEX Final IoT Monitoring Dashboard")
plt.xlabel("Sensor Reading")
plt.ylabel("Sensor Value")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("dashboard.png")

print("\nSensor data saved to sensor_data.csv")
print("Dashboard saved to dashboard.png")

plt.show()