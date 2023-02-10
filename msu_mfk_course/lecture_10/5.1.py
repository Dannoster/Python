import pandas as pd

df = pd.read_csv("input.csv").drop(columns=["ID"])

routes = df["Город отправления"] + df["Город прибытия"]
df["Уникальных маршрутов"] = routes
df.drop(columns=["Город отправления", "Город прибытия"], inplace=True)
df = df.groupby(["Номер борта"]).nunique()
df.sort_values(by=["Номер борта"], inplace=True)
df.sort_values(by=["Уникальных маршрутов"], ascending=False, inplace=True)
df.reset_index(inplace=True)

df.to_csv("output.csv", encoding="utf8", index=False)

# res = pd.DataFrame()
# res['Номер борта'] = df["Номер борта"]
# res["Уникальных маршрутов"] = df.values[:, 1]
# res.to_csv("output.csv", encoding="utf8", index=False)