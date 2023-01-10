import csv

# open the csv file
with open('datacs.csv','r') as file:
    # create a csv reader
   reader = csv.reader(file)

# iterate over the rows of the csv file
   for row in reader:
        # print the row as a list of strings
         print(row)