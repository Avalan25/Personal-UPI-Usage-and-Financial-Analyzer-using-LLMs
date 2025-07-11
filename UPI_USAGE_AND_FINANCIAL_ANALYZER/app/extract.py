import pdfplumber
import pandas as pd

def extract_pdf_data(pdf_path, password=None):
    data = []

    with pdfplumber.open(pdf_path, password=password) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    if row[0] is None or row[0].strip() == "Sr No":
                        continue
                    if len(row) < 6:
                        continue
                    sr_no = row[0].strip()
                    date = row[1].strip()
                    remarks = row[2].strip()
                    debit = (row[3] or '').replace('₹', '').replace(',', '').strip()
                    credit = (row[4] or '').replace('₹', '').replace(',', '').strip()
                    balance = (row[5] or '').replace('₹', '').replace(',', '').strip()
                    data.append([sr_no, date, remarks, debit, credit, balance])

    df = pd.DataFrame(data, columns=["Sr No", "Date", "Remarks", "Debit", "Credit", "Balance"])
    return df
