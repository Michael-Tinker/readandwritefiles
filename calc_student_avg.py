import csv
#Reading Stuffs
students = open("student_scores.csv","r")

#Writing Stuffs
CSVFILE = "student_avg.csv"
outfile = open(CSVFILE, "w", newline="")
writer = csv.writer(outfile, delimiter=",")
#Writing Fieldnames
fieldnames = ["Name","Average"]
writer.writerow(fieldnames)

#Reading Stuffs
student_file = csv.reader(students, delimiter=",")

#to skip a line if the file contains a header record
next(student_file)

#Reading through the file
for record in student_file:
    name = record[0]
    score1 = record[1]
    score2 = record[2]
    score3 = record[3]

    avg = round(((float(score1)+float(score2)+float(score3))/3), 2)
    
    row = [name, avg]
    print(row)
    writer.writerow(row)

outfile.close()
students.close()
