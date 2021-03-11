def schet_hogov(k):
    for i in range(len(spis_hodov)):
        for j in range(len(spis_hodov[i])):
            if spis_hodov[i][j] == k:
                h = 1
                if i > 0 and spis_hodov[i - 1][j] == 0 and spis_matriks[i - 1][j] != 3:
                    spis_hodov[i - 1][j] = k + h
                if j > 0 and spis_hodov[i][j - 1] == 0 and spis_matriks[i][j - 1] != 3:
                    spis_hodov[i][j - 1] = k + h
                if i < len(spis_hodov) - 1 and spis_hodov[i + 1][j] == 0 and spis_matriks[i + 1][j] != 3:
                    spis_hodov[i + 1][j] = k + h
                if j < len(spis_hodov[i]) - 1 and spis_hodov[i][j + 1] == 0 and spis_matriks[i][j + 1] != 3:
                    spis_hodov[i][j + 1] = k + h






# a = input()
# n = int(a[0])  # колличество строк
# m = int(a[-1])  # колличество символов в строке
# spis_matriks = []
#
# for i in range(n):
#    b = input()
#    rilli = []
#    for j in b:
#        rilli.append(j)
#    spis_matriks.append(rilli)

n = 13  # ненужно!
m = 13  # ненужно!
spis_matriks = [[1, 1, 1, 1, 1, 1, 1, 3, 2, 2, 2, 2, 2, 2],
                [1, 1, 3, 1, 1, 1, 1, 3, 1, 1, 1, 2, 2, 2],
                [1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1],
                [1, 1, 3, 3, 3, 3, 3, 3, 3, 2, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 3, 2, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 3, 2, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 3, 2, 1, 1, 1, 1],
                [1, 1, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 2, 2, 3, 1, 1, 1, 1, 1]]

start = 0, 0  # это стартовая позиция
end = n, m  # это конечная позиция

spis_hodov = []
for i in range(len(spis_matriks)):
    spis_hodov.append([])
    for j in range(len(spis_matriks[i])):
        spis_hodov[-1].append(0)

i, j = start
spis_hodov[i][j] = 1
k = 0

while spis_hodov[end[0]][end[1]] == 0:
    k += 1
    schet_hogov(k)

for i in spis_hodov:
    print("")
    for j in i:
        print(j, end="\t")
