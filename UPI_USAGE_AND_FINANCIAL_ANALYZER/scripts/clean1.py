import pdfplumber
import pandas as pd

# Define the PDF path and password
pdf_path = r"C:\\Users\\91902\\Desktop\\Vs_code\\FINAL PROJECT\\staement.PDF"
pdf_password = "aval1601"

data = []

with pdfplumber.open(pdf_path, password=pdf_password) as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()

        for table in tables:
            for row in table:
                if row[0] is None or row[0].strip() == "Sr No":
                    continue

                if len(row) < 6:
                    continue

                sr_no = row[0].strip()

                # Try parsing the date safely
                try:
                    parsed_date = pd.to_datetime(row[1].strip(), dayfirst=True, errors='coerce')
                    date = parsed_date.strftime('%Y-%m-%d') if not pd.isna(parsed_date) else ''
                except Exception:
                    date = ''

                remarks_raw = row[2].strip()
                remarks = remarks_raw[:50]  # Truncate long remarks

                debit = (row[3] or '').replace('₹', '').replace(',', '').strip()
                credit = (row[4] or '').replace('₹', '').replace(',', '').strip()
                balance = (row[5] or '').replace('₹', '').replace(',', '').strip()

                # Infer debit/credit if missing
                if not debit and not credit:
                    if 'DR' in remarks_raw.upper():
                        debit = '0.00'
                    elif 'CR' in remarks_raw.upper():
                        credit = '0.00'

                data.append([sr_no, date, remarks, debit, credit, balance])

# Convert to DataFrame
df = pd.DataFrame(data, columns=["Sr No", "Date", "Remarks", "Debit", "Credit", "Balance"])

# Save as cleaned CSV
df.to_csv("cleaned_statement.csv", index=False)
print("✅ Cleaned CSV created: cleaned_statement.csv")
