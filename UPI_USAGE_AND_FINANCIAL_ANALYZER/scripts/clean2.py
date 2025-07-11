import pandas as pd

# Load the cleaned CSV
df = pd.read_csv("cleaned_statement.csv")

# Convert numeric columns to floats
df["Debit"] = pd.to_numeric(df["Debit"], errors="coerce").fillna(0)
df["Credit"] = pd.to_numeric(df["Credit"], errors="coerce").fillna(0)
df["Balance"] = pd.to_numeric(df["Balance"], errors="coerce").fillna(0)

# Convert Date to datetime
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Create Year-Month column
df["YearMonth"] = df["Date"].dt.to_period("M")

# ---------------------------
# 1️⃣ Monthly Debit & Credit Totals
# ---------------------------
monthly_summary = df.groupby("YearMonth")[["Debit", "Credit"]].sum().reset_index()
print("\n=== Monthly Total Debit and Credit ===")
print(monthly_summary)

# ---------------------------
# 2️⃣ Most Frequent Payees or Merchants
# ---------------------------
# We'll assume the first word or UPI ID in Remarks indicates the merchant
df["Merchant"] = df["Remarks"].apply(lambda x: x.split("/")[3] if "/" in x and len(x.split("/")) > 3 else x[:15])

merchant_counts = df["Merchant"].value_counts().head(10)
print("\n=== Top 10 Frequent Merchants/Payees ===")
print(merchant_counts)

# ---------------------------
# 3️⃣ Average Balance Over Time
# ---------------------------
average_balance = df["Balance"].mean()
print(f"\n=== Average Balance ===\n₹ {average_balance:,.2f}")
