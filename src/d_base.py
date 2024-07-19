import pandas as pd
import csv
from datetime import datetime



class CSV:
    CSV_FILE = "finance data.csv"

    @classmethod
    def init_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=["Date", "Amount", "Category", "Description"])
                    