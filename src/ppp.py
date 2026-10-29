import pandas as pd
import math

pizzas = pd.read_csv("data\\pizzas.csv")

pizzas["Area"] = (pizzas["Size"] / 2) ** 2 * math.pi
pizzas["Price_per_SqInch"] = pizzas["Price"] / pizzas["Area"]

pizzas = pizzas.sort_values(by = ["Price_per_SqInch"])
print(pizzas)