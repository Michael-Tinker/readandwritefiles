import csv
from operator import delitem
#Reading Stuffs
customers = open("customers.csv","r")

#Writing Stuffs
CSVFILE = "customer_country.csv"
outfile = open(CSVFILE, "w", newline="")
writer = csv.writer(outfile, delimiter=",")
#Writing Fieldnames
fieldnames = ["FirstName","Lastname","Country"]
writer.writerow(fieldnames)

#Reading Stuffs
customer_file = csv.reader(customers, delimiter=",")

#to skip a line if the file contains a header record
next(customer_file)

#Reading through the file
count = 0
for record in customer_file:
    custid = record[0]
    firstname = record[1]
    lastname = record[2]
    city = record[3]
    country = record[4]
    phone = record[5]
    count += 1
    row = [firstname, lastname, country]
    writer.writerow(row)

print(count)