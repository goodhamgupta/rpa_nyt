import pandas as pd


def write_to_excel(records, sheet_name="result"):
    df = pd.DataFrame(records)
    df.to_excel("output/nytimes.xlsx", sheet_name=sheet_name, index=False)
