import sqlite3
import pandas as pd
import numpy as np

#dane w numpy

names = np.array(["Jan","Anna","Piotr","Maria"])
ages = np.array(["18","46","68","32"])
points = np.array([80,67,77,34])


df = pd.DataFrame({"name":names,"age":ages,"points":points})

print(df)

#połączenie z bazą sqlite
conn = sqlite3.connect("students.db")
df.to_sql("students",conn,if_exists="replace",index=False)

print("Dane z tabeli SQL")
query = """
SELECT name,age FROM students
WHERE points >= 80
"""

df_from_sql = pd.read_sql_query(query,conn)

print(df_from_sql)

conn.close()
