import pandas as pd
import csv
from datetime import datetime
from entry import *

class CSV:
    CSV_FILE = "finance data.csv"
    COLUMNS = ["Date", "Amount", "Category", "Description"] 

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns = cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index = False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "Date": date,
            "Amount": amount,
            "Category": category,
            "Description": description
        }

        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = cls.COLUMNS)
            writer.writerow(new_entry)

        print("Entry added successfully") 

def add_transaction():
    CSV.initialize_csv()
    date = get_date("Enter date in mm-dd-yyyy: ")
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)


add_transaction()