# import the python pandas package
from sys import argv

import pandas as pd
from pathlib import Path


def json_to_excel(source, target_file, sheet_name):
    # Accepts Source json file and target xl file and sheet name
    # Converts the json file to xl file
    # if the sheet exists, append the data
    df = pd.read_json(source)
    excel_file = Path(target_file)
    # If doesnt Exists, Create it else Append the Content

    if not excel_file.is_file():
        with pd.ExcelWriter(target_file, ) as writer:
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    else:
        xls_file = pd.ExcelFile(target_file)
        with pd.ExcelWriter(target_file, mode="a", if_sheet_exists='overlay', engine="openpyxl") as writer:
            if sheet_name in xls_file.sheet_names:
                df.to_excel(writer, sheet_name=sheet_name, startrow=writer.sheets[sheet_name].max_row, index=False, header=False)
            else:
                df.to_excel(writer, sheet_name=sheet_name, index=False)

json_to_excel(argv[1], argv[2], argv[3])