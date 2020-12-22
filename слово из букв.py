rows = int(input())
cols = int(input())
table = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(input())
    table.append(row)
for i in range(rows):
    for j in range(cols):
        print(table[i][j], end='\t')
    print()
