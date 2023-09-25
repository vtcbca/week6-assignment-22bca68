import csv

r = []
header = ["Student ID", "Student Name", "Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]
r.append(header)


for i in range(1,11):
    s_id = i
    s_name = input(f"Enter name for Student {i}: ")
    marks = []
    for j in range(5):
        sub_mark = int(input(f"Enter marks for Subject {j+1} for Student {i}: "))
        marks.append(sub_mark)
    r.append([s_id, s_name] + marks)


with open("result.csv", "w", newline="") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerows(r)



with open("result.csv", "r") as f:
    csv_reader = csv.reader(f)
    r_data = list(csv_reader)

    header = r_data[0]
    header.extend(["Total Marks", "Grade"])

    for row in rdata[1:]:
        total_marks = sum(map(int, row[2:7]))
        row.extend([total_marks, "A" if total_marks >= 250 else "B" if total_marks >= 200 else "C"])

    with open("result.csv", "w", newline="") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerows(r_data)


with open("result.csv", "r") as f:
    csv_reader = csv.reader(f)
    next(csv_reader)  
    students = []

    for row in csv_reader:
        s_id = int(row[0])
        s_name = row[1]
        total_marks = int(row[-2])
        percentage = (total_marks / 500) * 100
        students.append((sid, sname, percentage))

    top_students = sorted(students, key=lambda x: x[2], reverse=True)[:3]

    print("Top 3 Students:")
    for student in top_students:
        print(f"Student ID: {student[0]}, Name: {student[1]}, Percentage: {student[2]:.2f}%")
