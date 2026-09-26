import pandas as pd


INPUT_FILE = "customer_shopping_behavior.csv"
OUTPUT_FILE = "customer_shopping_behavior_cleaned.csv"


print("Loading data...")
df = pd.read_csv(INPUT_FILE)
print(f"Loaded {len(df):,} rows and {len(df.columns)} columns.\n")

print("First five rows:")
print(df.head())

print("\nSummary statistics:")
print(df.describe(include="all"))

print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Fill missing review ratings with the median rating for the customer's category.
df["Review Rating"] = (
    df.groupby("Category")["Review Rating"]
    .transform(lambda values: values.fillna(values.median()))
)

print("\nMissing values after filling review ratings:")
print(df.isnull().sum())

# Standardize column names.
df.columns = df.columns.str.lower().str.replace(" ", "_")
df = df.rename(columns={"purchase_amount_(usd)": "purchase_amount"})

print("\nCleaned column names:")
print(list(df.columns))

# Divide customers into four age groups based on age quartiles.
age_labels = ["young", "teenager", "adult", "senior"]
df["age_group"] = pd.qcut(df["age"], q=4, labels=age_labels)

print("\nAge groups:")
print(df[["age", "age_group"]].head(15))
print("\nNumber of customers in each age group:")
print(df["age_group"].value_counts().sort_index())

frequency_mapping = {
    "Fortnightly": 14,
    "Weekly": 7,
    "Monthly": 30,
    "Annually": 365,
    "Quarterly": 90,
    "Bi-Weekly": 14,
    "Every 3 Months": 90,
}

df["frequency_in_days"] = df["frequency_of_purchases"].map(frequency_mapping)

print("\nPurchase frequency converted to days:")
print(df[["frequency_of_purchases", "frequency_in_days"]].head(10))

# Remove duplicate frequency columns if they exist in another version of the CSV.
df = df.drop(
    columns=["frequency_purchases_days", "purchase_frequency_days"],
    errors="ignore",
)

# Check whether these two columns contain the same information before dropping one.
promo_matches_discount = (
    df["promo_code_used"] == df["discount_applied"]
).all()
print(f"\nPromo code and discount columns contain the same values: {promo_matches_discount}")

if promo_matches_discount:
    df = df.drop(columns="promo_code_used")
    print("Dropped the duplicate 'promo_code_used' column.")

print("\nFinal data preview:")
print(df.head())

print("\nFinal columns:")
print(list(df.columns))

print("\nMissing values in the final dataset:")
print(df.isnull().sum())

df.to_csv(OUTPUT_FILE, index=False)
print(f"\nCleaned data saved to '{OUTPUT_FILE}'.")
