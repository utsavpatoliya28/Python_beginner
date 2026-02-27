
def generatetable(i):
    table = ""
    for j in range(1, 11):
        table += f"{i} * {j} = {i*j}\n"

    with open(f"tables/table_{i}.txt", "w") as f:
        f.write(table)

for i in range(2, 21):
    generatetable(i)

