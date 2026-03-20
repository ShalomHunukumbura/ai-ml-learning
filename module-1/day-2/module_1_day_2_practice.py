import pandas as pd

df =  pd.read_csv("students.csv")
# print(df,"\n")

# data inspecting

# print(df.head(),"\n")
# print(df.head(3),"\n")
# print(df.info(),"\n")
# print(df.describe())

print("-"*100)

print("\nfill missing values\n")

df["math"] = df["math"].fillna(df["math"].mean())
df["science"] = df["science"].fillna(df["science"].mean())
df["attendance"] = df["attendance"].fillna(df["attendance"].mean())
# print(df,"\n\n\n")

# print("advanced filtering: students with good attendance and marks\n")

# filtered = df[(df["attendance"] > 80 ) & (df["math"] > 60 )]
# print(filtered)

df["name"] = df["name"].str.lower()
print("\n",df)

df = df.drop_duplicates()

df["average score"] =  df["math"] + df["science"] / 2
df["performance"] =  df["average score"].apply(lambda x: "good" if x > 70 else "poor")


# print("\n",df)

# bonus_df = pd.read_csv("attendance_bonus.csv")

# bonus_df["name"] = bonus_df["name"].str.lower()

# merged = pd.merge(df, bonus_df, on="name")


# print("\n\n\n", merged)

df = df.sort_values(by="average score", ascending=False)
df["rank"] = df["average score"].rank(ascending=False)
print("\n\n", df)
