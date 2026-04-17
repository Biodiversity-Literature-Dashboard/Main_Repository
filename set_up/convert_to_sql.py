
import sqlite3 as lite
import pandas as pd

def convert_excel_to_sql(file: str):
    """ create SQLite database from """
    conn = lite.connect("./database/database.db")
    all_sheets = pd.read_excel(file, sheet_name=None)
    sheets = all_sheets.keys()
    for sheet_name in sheets:
        sheet = pd.read_excel(file,sheet_name=sheet_name)
        sheet.to_sql(sheet_name.replace(" ", "_"),conn, index=False)

if __name__ == "__main__":
    # change this to include the correct file
    convert_excel_to_sql('data/xlsx(dont use)/Ridley_et_al_13750_2022_279_MOESM4_ESM.xlsx')
