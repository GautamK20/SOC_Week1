a = [['', 1, 5, '', '', 2, 8, '', 9], ['', '', '', '', '', 1, 6, '', 7], ['', 7, '', '', '', 8, 4, '', ''], ['', '', 6, '', 1, 7, '', 4, 5],
     ['', 5, 3, '', '', 4, 7, '', ''], [8, 4, '', '', 9, 5, '', 6, 2], ['', '', 4, 1, 7, '', '', 8, 6], [7, 6, '', 5, 2, '', 9, 1, ''],
     [5, 9, 1, '', 8, 6, '', '', '']]
print("Initial Grid:")
for i in range(9):
    print(a[i])

set1 = [[{1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}],
        [{1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}],
        [{1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}]]

count = 0

for i in range(9):
    for j in range(9):
        if a[i][j] != '':
            set1[int(i/3)][int(j/3)].remove(a[i][j])
            count += 1

while count < 81:
    for i in range(9):
        for j in range(9):
            temp = set()
            if a[i][j] == '':
                for k in range(9):
                    if a[i][k] != '':
                        temp.add(a[i][k])
                    if a[k][j] != '':
                        temp.add(a[k][j])

                if len(set1[int(i/3)][int(j/3)] - temp) == 1:
                    a[i][j] = (set1[int(i/3)][int(j/3)] - temp).pop()
                    set1[int(i/3)][int(j/3)].remove((set1[int(i/3)][int(j/3)] - temp).pop())
                    count += 1

            else:
                continue
        else:
            continue

print("Solved Grid:")

for p in range(9):
    print(a[p])
