def schet_hogov(k):
    for i in range(len(spis_hodov)):  # i - строка (горизонт)
        for j in range(len(spis_hodov[i])):  # j (вертикатль) эл. строки
            if spis_hodov[i][j] == k:
                #  с суши на сушу
                if i > 0 and spis_hodov[i - 1][j] == 0 \
                         and spis_matriks[i - 1][j] == 1:
                    spis_hodov[i - 1][j] = k + 1
                if j > 0 and spis_hodov[i][j - 1] == 0 \
                         and spis_matriks[i][j - 1] == 1:
                    spis_hodov[i][j - 1] = k + 1
                if i < len(spis_hodov) - 1 \
                        and spis_hodov[i + 1][j] == 0 \
                        and spis_matriks[i + 1][j] == 1:
                    spis_hodov[i + 1][j] = k + 1
                if j < len(spis_hodov[i]) - 1 \
                        and spis_hodov[i][j + 1] == 0 \
                        and spis_matriks[i][j + 1] == 1:
                    spis_hodov[i][j + 1] = k + 1
                # с воды на воду
                if i > 0 and spis_hodov[i - 1][j] == 0 \
                         and spis_matriks[i][j] == 2 \
                         and spis_matriks[i - 1][j] == 2:
                    spis_hodov[i - 1][j] = k
                if j > 0 and spis_hodov[i][j - 1] == 0 \
                         and spis_matriks[i][j] == 2 \
                         and spis_matriks[i][j - 1] == 2:
                    spis_hodov[i][j - 1] = k
                if i < len(spis_hodov) - 1 \
                        and spis_hodov[i + 1][j] == 0 \
                        and spis_matriks[i][j] == 2 \
                        and spis_matriks[i + 1][j] == 2:
                    spis_hodov[i + 1][j] = k
                if j < len(spis_hodov[i]) - 1 \
                        and spis_hodov[i][j + 1] == 0 \
                        and spis_matriks[i][j] == 2 \
                        and spis_matriks[i][j + 1] == 2:
                    spis_hodov[i][j + 1] = k
                # с суши на воду
                if i > 0 and spis_hodov[i - 1][j] == 0 \
                         and spis_matriks[i][j] == 1 \
                         and spis_matriks[i - 1][j] == 2:
                    spis_hodov[i - 1][j] = k + 1
                if j > 0 and spis_hodov[i][j - 1] == 0 \
                         and spis_matriks[i][j] == 1 \
                         and spis_matriks[i][j - 1] == 2:
                    spis_hodov[i][j - 1] = k + 1
                if i < len(spis_hodov) - 1 \
                        and spis_hodov[i + 1][j] == 0 \
                        and spis_matriks[i][j] == 1 \
                        and spis_matriks[i + 1][j] == 2:
                    spis_hodov[i + 1][j] = k + 1
                if j < len(spis_hodov[i]) - 1 \
                        and spis_hodov[i][j + 1] == 0 \
                        and spis_matriks[i][j] == 1 \
                        and spis_matriks[i][j + 1] == 2:
                    spis_hodov[i][j + 1] = k + 1


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
end = -1, -1  # это конечная позиция

spis_hodov = []  # пустая матрийа возможных ходов
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

for i in spis_hodov:  # вывод красивой таблицей
    print("")
    for j in i:
        print(j, end="\t")
