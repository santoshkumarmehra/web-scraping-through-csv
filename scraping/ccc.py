import csv



with open('scrap.csv','w') as f1:
    w = csv.DictWriter(f1,fieldnames=["product name","price","shipping"])
    w.writeheader()


