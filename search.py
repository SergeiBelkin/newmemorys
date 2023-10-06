import csv
import one
# a = one.writer()
# print(a)
fileBase = "Base.csv"
with open(fileBase , "a") as file:
    a = one.writer()
    print(a)
    columns = ["DATE","TITLE","TEXT"]
    read = csv.DictWriter(file, fieldnames = columns)    
    read.writerow(a)