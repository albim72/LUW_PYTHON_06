import pandas as pd
import numpy as np

#dane - numpy
products = np.array(["Laptop","Monitor","Klawiatura","Mysz"])
prices = np.array([4670,899,212,121])
quantities = np.array([2,3,4,4])

df = pd.DataFrame({
    "product": products,
    "price": prices,
    "quantity": quantities
})

#dodawamnie kolumny obliczeniowej

df["total_value"] = df["price"]*df["quantity"]

print(df)

#zapis do pliki excel

df.to_excel("poducts.xlsx", sheet_name="Products", index=False)

print("dane z pliku excel!")

df_from_excel = pd.read_excel("poducts.xlsx", sheet_name="Products")
print(df_from_excel)

#analiza
total_warehouse_value = df_from_excel["total_value"].sum()
print(f"total_warehouse_value {total_warehouse_value}")
