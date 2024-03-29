from sys import argv

import pandas as pd

# First DataFrame
source1 = {'id': ['A01', 'A02', 'A03', ''],
                    'Name': ['ABC', 'PQR', 'DEF', 'GHI']}

# Second DataFrame
source2 = {'id': ['B05', 'B06', 'B07', 'B08'],
                    'Name': ['XYZ', 'TUV', 'MNO', 'JKL']}


# def myFun(arg1, *argv):
def myFun(target, sheet, *argv):
    print("First argument :", target)
    print("Second Argument :", sheet)
    appended_data = []
    for arg in argv:
        appended_data.append(pd.DataFrame(arg))
        print("Next argument through *argv :", appended_data)
    appended_data = pd.concat(appended_data)
    # print("Next argument through *argv :", appended_data)
# frames = [df1, df2]
# result = pd.concat(frames)
# print(result)
print(str(len(argv)) + "arguments")
myFun('target', 'sheet_name', source1, source2)
