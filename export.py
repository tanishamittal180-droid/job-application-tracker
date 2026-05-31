import pandas as pd

def export_excel(df):
    path = "applications.xlsx"
    df.to_excel(path,index=False)
    return path