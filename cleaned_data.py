import pandas as pd


aggregated = pd.read_csv("data/processed/aggregated.csv")
aggregated["date"] = pd.to_datetime(aggregated["date"])
print(aggregated["temperature_2m_mean"])

# Let's assume the simple baseline of having the same temperature at J+1 than J
# We will compute the average error
aggregated["next_day_temperature_max"] = aggregated["temperature_2m_max"].shift(-1)
aggregated = aggregated.dropna()
