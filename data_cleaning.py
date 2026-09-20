import pandas as pd

data = pd.read_csv("EDA_Practice_Dataset.csv")
df = pd.DataFrame(data)



print("Practice of Data Cleaning")
print(df)

print(df.isnull().sum())
# df_drop = df.dropna()
# print(df_drop)

df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)
df['City'].fillna(df['City'].mode()[0], inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
df['Purchase_Amount'].fillna(df['Purchase_Amount'].mean(), inplace=True)
df['Is_Member'].fillna(df['Is_Member'].mode()[0], inplace=True)
df['Purchase_Date'].fillna(df['Purchase_Date'].mode()[0], inplace=True)


print(df.isnull().mean() * 100)
print(df.to_string())

# Hence data has been cleaned