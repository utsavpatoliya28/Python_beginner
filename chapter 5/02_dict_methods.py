marks = { 
    "Utsav" : 100,
    "Kavy"  : 56,
    "Rohan" : 33,
    0: "Utsav"
}

#print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Utsav": 99, "Trisha": 100})
print(marks)

print(marks.get("Utsav2"))#It gives none
print(marks["Utsav2"])#It gives error

