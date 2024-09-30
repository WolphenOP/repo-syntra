data =[
    ["Jan", 8, 7, 5],
    ["Pier", 9, 7, 4],
    ["Tjoris", 7, 8, 6]
]
for row in data:
    total = sum(row[1:])
    row.append(total)
for rij in data:
    for item in rij:
        print(item,end="\t")
    print(" ")