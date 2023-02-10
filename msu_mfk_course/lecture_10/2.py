import pandas as pd

df = pd.read_csv("input.csv")

celsius = df["temperature_c"]
celsius = round(9/5 * celsius + 32)
celsius = [int(num) for num in celsius]
df["temperature_f"] = celsius

df.to_csv("output.csv")