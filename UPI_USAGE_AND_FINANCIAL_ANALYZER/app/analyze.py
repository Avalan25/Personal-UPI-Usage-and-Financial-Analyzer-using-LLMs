def summarize(df):
    monthly = df.groupby("YearMonth")[["Debit", "Credit"]].sum()
    categories = df.groupby("Category")["Debit"].sum()
    avg_balance = df["Balance"].mean()

    summary = f"Monthly Spend:\n{monthly}\n\nBy Category:\n{categories}\n\nAvg Balance: ₹{avg_balance:,.2f}"
    return summary
