import pandas as pd
import numpy as np

#create data
# data ={
#	"name":["Asha","Jake","Ally"],
#	"age":[25,21,32],
#	"salary":[50000,45000,90000]
# }

# create dataframe(a.k.a a table)
# df = pd.DataFrame(data)
#print(df)
# print("-"*100)

# print(df.head()) # first rows
# print("-"*50)
# print(df.info()) # structure
# print("-"*50)
# print(df.describe()) # statistics
# print("-"*50)
# print(df["age"]) # single column
# print("-"*50)
# multiple columns
# print(df[["age","name"]])

# high salary (filtering data)
# high_salary = df[df["salary"]>50000]
# print(high_salary)

# feature engineering
# df["yearly_salary"] = df["salary"] * 12
# print(df)



# handling missing data
# df.loc[2,"salary"] = np.nan
# print(df)

# fill missing data
# df["salary"] = df["salary"].fillna(df["salary"].mean())

# print(df)

# sorting
# df_sorted = df.sort_values(by="salary", ascending=False)
# print(df_sorted)


#  grouping
# grouped = df.groupby("age")["salary"].mean()
# print(grouped)

print("-"*50+ " " + "TASK 1" + "-" *50)

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ishaan", "Julia"],
    "marks": [85, 72, 90, 60, 88, 55, 78, 92, 67, 81],
    "attendance": [90, 80, 95, 70, 92, 65, 85, 98, 75, 88]
}


df = pd.DataFrame(data)
print(df)

print("\nFind students with marks>70\n")
high_mark_students = df[df["marks"] > 70]
print("Students with high marks:\n ",high_mark_students)

print("\nAdd new column: grade\n")

def get_grade(marks):
	if marks>=80:
		return "A"
	elif marks>=60:
		return "B"
	elif marks>50:
		return "C"
	else:
		return "D"
df["grade"] = df["marks"].apply(get_grade)
print("\nTable with grades column:\n", df)

print("\nsort by marks\n")
df_sort = df.sort_values(by="marks", ascending=False)
print(df_sort)

print("-"*50+"TASK 2"+"-"*50)

data2 = {
    "product": ["Laptop", "Phone", "Headphones", "Keyboard", "Mouse", "Monitor", "Tablet", "Charger", "Speaker", "Webcam"],
    "price": [1200, 800, 150, 100, 50, 300, 600, 25, 200, 120],
    "quantity": [5, 10, 25, 15, 30, 8, 7, 40, 12, 9]
}

df2 = pd.DataFrame(data2)
print("\n", df2)

print("\ncreate total value column\n")

df2["total value"] = df2["price"] * df2["quantity"]
print(df2)

print("\nfind most valuable product\n")
df2_most_valuable = df2.sort_values(by="total value", ascending=False).head(1)
print("most valuable\n",df2_most_valuable)
df2_top3 = df2.sort_values(by="total value", ascending=False).head(3)
print("top 3 most valuable\n", df2_top3)

print("\nfiler products grearer than 5000\n")
print(df2[df2["total value"]> 5000])
