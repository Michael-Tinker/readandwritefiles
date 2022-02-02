import csv

customers = open("EmployeePay.csv","r")

pay_file = csv.reader(customers, delimiter=",")

#to skip a line if the file contains a header record
next(pay_file)

for record in pay_file:
    employeeid = record[0]
    firstname = record[1]
    lastname = record[2]
    salary = record[3]
    bonus = record[4]

    float_salary = float(salary)
    format_salary = format(float_salary, ",.2f")

    float_bonus = float(bonus)
    #bonus_percentage = format(float_bonus,".2%")

    bonus_dollars = float_salary * float_bonus
    format_bonus = format(bonus_dollars, ",.2f")

    totalpay = (float(bonus) + 1)*float(salary)
    round_totalpay = round(totalpay, 2)
    format_totalpay = format(round_totalpay, ",.2f")

    print("Fname:     " + firstname + "\nLname:     " + lastname + "\nSalary:    $" + format_salary + "\nBonus:     $" + format_bonus + "\nTotal pay: $" + str(format_totalpay))
    input()

