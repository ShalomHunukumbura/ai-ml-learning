import pandas as pd
import numpy as np

data = {
    "name": ["Asha", "Nimal", "Kamal", "Sara", "John"],
    "math": [78, 56, 90, None, 67],
    "science": [88, 61, 84, 75, None],
    "attendance": [92, 81, 96, 89, 70]
}

df =  pd.DataFrame(data)
print(df)

print("\nMissing data filled\n")
df[["math", "science"]] = df[["math", "science"]].fillna(
df[["math","science"]].mean()
)
print(df)

print("\nnew column average score\n")
total_score = df["math"] + df["science"] 
df["average score"] = total_score/2
print(df)

print("\ntop student\n")
top_student = df.sort_values(by="average score", ascending=False).head(1)
print(top_student)

print("\nstudents below 60\n")
below_75 = df["average score"] < 75
print(df[below_75])

print("\naverage class score\n")
average_class_score = df["average score"].mean()
print(average_class_score)
