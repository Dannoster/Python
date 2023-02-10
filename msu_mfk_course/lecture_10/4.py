import pandas as pd

df = pd.read_csv("input.csv").drop(columns=["ID"])

mask = df["Тип операции"] == "Вывоз"
out_column = -1 * df[mask]["Объем груза"]
df.update(out_column)
df.drop(columns=["Тип операции"], inplace=True)
df = df.groupby(["Фамилия водителя"]).sum().sort_values(by=["Объем груза"], ascending=False).astype({'Объем груза':'int'})
df.reset_index(inplace=True)
# print(df)

df.to_csv("output.csv")