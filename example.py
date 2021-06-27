
import csv

csv_path = "./Resources/election_results.csv"

with open(csv_path,"r") as raw_csv:
    # clean_csv = list(raw_csv)
    clean_csv = csv.reader(raw_csv)
    for row in clean_csv:
        print(row)
        
    
    # print ("====================================")
    # print (list(clean_csv))
    # print ("====================================")