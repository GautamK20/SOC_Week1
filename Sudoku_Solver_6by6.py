a = [['', '', 3, '', 1, ''], [5, 6, '', 3, 2, ''], ['', 5, 4, 2, '', 3], [2, '', 6, 4, 5, ''], ['', 1, 2, '', 4, 5],
     ['', 4, '', 1, '', '']]
print("Initial Grid:")
for i in range(6):
    print(a[i])

set1 = [[{1, 2, 3, 4, 5, 6}, {1, 2, 3, 4, 5, 6}], [{1, 2, 3, 4, 5, 6}, {1, 2, 3, 4, 5, 6}], [{1, 2, 3, 4, 5, 6}, {1, 2, 3, 4, 5, 6}]]

count = 0

for i in range(6):
    for j in range(6):
        if a[i][j] != '':
            set1[int(i/2)][int(j/3)].remove(a[i][j])
            count += 1

while count < 36:
    for i in range(6):
        for j in range(6):
            temp = set()
            if a[i][j] == '':
                for k in range(6):
                    if a[i][k] != '':
                        temp.add(a[i][k])
                    if a[k][j] != '':
                        temp.add(a[k][j])

                if len(set1[int(i/2)][int(j/3)] - temp) == 1:
                    a[i][j] = (set1[int(i/2)][int(j/3)] - temp).pop()
                    set1[int(i/2)][int(j/3)].remove((set1[int(i/2)][int(j/3)] - temp).pop())
                    count += 1

            else:
                continue
        else:
            continue

print("Solved Grid:")

for p in range(6):
    print(a[p])
