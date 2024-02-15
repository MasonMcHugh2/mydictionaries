student = {"name": 'Mason McHugh',
"age": 21,
"major": 'Finance and MIS',
"hobbies": 'Beach volleyball, working out, hanging out with friend'}

student['state'] = 'Texas'

student['age'] += 1

for d in student:
    print(f"{d:7}:  {student[d]}")