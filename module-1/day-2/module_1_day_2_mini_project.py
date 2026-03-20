import pandas as pd

df = pd.read_csv("messy_students.csv")
print(df)

## normalize columns names
df.columns = df.columns.str.lower().str.strip()

# clean name column
df["name"] = df["name"].str.lower().str.strip()

# replace fake null values with real missing values
df["name"] = df["name"].replace(["NULL","null",""],pd.NA)

# convert score columns to numeric
for col in ["math", "science", "attendance"]:
	df[col] = pd.to_numeric(df[col], errors="coerce")

print("\n\n\n\n\n\n=== AFTER TYPE CLEANING ===")
print(df.head(),"\n\n")
# print("\n",df)

# remove rows where name is missing
df = df.dropna(subset=["name"])

# fill missing marks with subject averages
df["math"] = df["math"].fillna(df["math"].mean())
df["science"] = df["science"].fillna(df["science"].mean())

# fill missing attendance with median attendance
df["attendance"] = df["attendance"].fillna(df["attendance"].median())

# round numeric column
df["math"] = df["math"].round(1)
df["science"] = df["science"].round(1)
df["attendance"] = df["attendance"].round(1)

print("\n=== CLEANED DATA === \n")
print(df.head())
print("\n shape after cleaning: ", df.shape)

# save cleaned data to new csv
df.to_csv("cleaned_students.csv", index=False)

# creare feature average_score and performance
df["average score"] = df["math"] + df["science"] /2
df["performance"] = df["average score"].apply(lambda x: "good" if x > 70 else "poor")

# sort and rank
df = df.sort_values(by="average score", ascending=False)
df["rank"] = df["average score"].rank(ascending=False)
print("\n",df)
