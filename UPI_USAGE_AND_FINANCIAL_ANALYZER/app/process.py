import pandas as pd

def clean_and_categorize(df):
    df["Debit"] = pd.to_numeric(df["Debit"], errors="coerce").fillna(0)
    df["Credit"] = pd.to_numeric(df["Credit"], errors="coerce").fillna(0)
    df["Balance"] = pd.to_numeric(df["Balance"], errors="coerce").fillna(0)
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["YearMonth"] = df["Date"].dt.to_period("M")

    def categorize(remark):
        r = remark.lower()
        if any(k in r for k in ['amazon', 'flipkart', 'shopping']): return "Shopping"
        elif any(k in r for k in ['zomato', 'swiggy', 'food']): return "Food"
        elif any(k in r for k in ['electricity', 'bill', 'gas']): return "Utilities"
        elif any(k in r for k in ['rent', 'landlord']): return "Rent"
        elif any(k in r for k in ['salary', 'credit']): return "Income"
        else: return "Others"

    df["Category"] = df["Remarks"].apply(categorize)
    return df
