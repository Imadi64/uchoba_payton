def equation(a, b):
    a = a.split(";")
    b = b.split(";")
    a[0] = float(a[0])
    a[1] = float(a[1])
    b[0] = float(b[0])
    b[1] = float(b[1])
    x1, y1 = a
    x2, y2 = b
    if x1 == x2:
        print(x1)
    elif y1 == y2:
        print(y1)
    else:
        k = (y2 - y1) / (x2 - x1)
        print(k, y2 - k * x2)





equation("0;0", "1;1")
equation("0;0", "0;4")
equation("4;6.9", "-5.2;6.9")

