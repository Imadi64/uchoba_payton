def line(s, t):
    for i in s:
        if i == "+":
            s = s.split("x+")
            break
        if i == "-":
            s = s.split("x")
            break
    k, b = float(s[0]), float(s[1])
    t = t.split(";")
    x = float(t[0])
    y = k * x + b
    if float(t[1]) == y:
        print(True)
    else:
        print(False)


line("1x+6", "1;7")
line("5x-10", "5;-9")
line("0x+7", "3;7")
line("3.5x+0", "2;7")
line("-0.24x-9.4", "8.6;-11.464")