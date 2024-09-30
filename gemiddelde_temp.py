temp = [[12,9,6,3,3],[16,16,16,14,16]]
for row in temp:
    average = sum(row) / len(row)
    row.append(average)
print(temp)