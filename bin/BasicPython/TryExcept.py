import re
txt = "There was Rain in Spain"
try:
    x= re.search("ain$", txt)
    x.string()
except Exception as err:
    print(type(err))
else:
    print("No errors Found")
finally:
    print("Processing Completed")

try:
    x= re.search("ain$", txt)
    x.string()
except (RuntimeError, TypeError, NameError) as err:
    print(type(err))
else:
    print("No errors Found")
finally:
    print("Processing Completed")