students ={
    "001":"Amy",
    "002":"Bob",
    "003":"Cc",
    "004":"David",
    "005":"Eve"
}
filtered_students={k:v for k,v in students.items()if int(k[-1])%2!=0}
print(filtered_students)