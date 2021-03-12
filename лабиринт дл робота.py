def schet_hogov(k):
    for i in range(len(spis_hodov)):
        for j in range(len(spis_hodov[i])):
            if spis_hodov[i][j] == k:
                if i > 0 and spis_hodov[i - 1][j] == 0 and \
                        spis_matriks[i - 1][j] == 1:
                    spis_hodov[i - 1][j] = k + 1
                if j > 0 and spis_hodov[i][j - 1] == 0 and \
                        spis_matriks[i][j - 1] == 1:
                    spis_hodov[i][j - 1] = k + 1
                if i < len(spis_hodov) - 1 and spis_hodov[i + 1][j] == 0 and \
                        spis_matriks[i + 1][j] == 1:
                    spis_hodov[i + 1][j] = k + 1
                if j < len(spis_hodov[i]) - 1 and spis_hodov[i][j + 1] == 0 \
                        and spis_matriks[i][j + 1] == 1:
                    spis_hodov[i][j + 1] = k + 1
                if i > 0 and spis_hodov[i - 1][j] == 0 and \
                        spis_matriks[i - 1][j] == 2:
                    spis_hodov[i - 1][j] = k
                if j > 0 and spis_hodov[i][j - 1] == 0 and \
                        spis_matriks[i][j - 1] == 2:
                    spis_hodov[i][j - 1] = k
                if i < len(spis_hodov) - 1 and spis_hodov[i + 1][j] == 0 and \
                        spis_matriks[i + 1][j] == 2:
                    spis_hodov[i + 1][j] = k
                if j < len(spis_hodov[i]) - 1 and spis_hodov[i][j + 1] == 0 \
                        and spis_matriks[i][j + 1] == 2:
                    spis_hodov[i][j + 1] = k


a = input()
n = int(a[0])  # колличество строк
m = int(a[-1])  # колличество символов в строке
spis_matriks = []
for i in range(n):
    b = input()
    rilli = []
    for j in b:
        rilli.append(int(j))
    spis_matriks.append(rilli)
start = 0, 0  # это стартовая позиция
end = n - 1, m - 1  # это конечная позиция
spis_hodov = []
for i in range(len(spis_matriks)):
    spis_hodov.append([])
    for j in range(len(spis_matriks[i])):
        spis_hodov[-1].append(0)
a, b = start
spis_hodov[a][b] = 1
k = 0
while spis_hodov[end[0]][end[1]] == 0:
    k += 1
    schet_hogov(k)
if spis_matriks[a][b] == 2:
    print(spis_hodov[-1][-1] - 1)
else:
    print(spis_hodov[-1][-1])
for i in spis_hodov:
    print("")
    for j in i:
        print(j, end="\t")
