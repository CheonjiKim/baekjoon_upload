credit = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}
total_grade = 0
total_acq_credit = 0
for i in range(0, 20):
    c_name, grade, acq_credit = map(str, input().split())
    grade = float(grade)
    if(acq_credit != "P"):
        total_grade += grade
        total_acq_credit += grade * credit[acq_credit]
print(total_acq_credit / total_grade)