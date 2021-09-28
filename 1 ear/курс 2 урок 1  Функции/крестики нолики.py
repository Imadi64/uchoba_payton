def tic_tac_toe(field):
    if field[0][0] == "x" and field[0][1] == "x" and field[0][2] == "x":
        print("x win")
    elif field[1][0] == "x" and field[1][1] == "x" and field[1][2] == "x":
        print("x win")
    elif field[2][0] == "x" and field[2][1] == "x" and field[2][2] == "x":
        print("x win")
    elif field[0][0] == "x" and field[1][0] == "x" and field[2][0] == "x":
        print("x win")
    elif field[0][1] == "x" and field[1][1] == "x" and field[2][1] == "x":
        print("x win")
    elif field[0][2] == "x" and field[1][2] == "x" and field[2][2] == "x":
        print("x win")
    elif field[0][0] == "x" and field[1][1] == "x" and field[2][2] == "x":
        print("x win")
    elif field[0][2] == "x" and field[1][1] == "x" and field[2][0] == "x":
        print("x win")
    else:
        if field[0][0] == "0" and field[0][1] == "0" and field[0][2] == "0":
            print("0 win")
        elif field[1][0] == "0" and field[1][1] == "0" and field[1][2] == "0":
            print("0 win")
        elif field[2][0] == "0" and field[2][1] == "0" and field[2][2] == "0":
            print("0 win")
        elif field[0][0] == "0" and field[1][0] == "0" and field[2][0] == "0":
            print("0 win")
        elif field[0][1] == "0" and field[1][1] == "0" and field[2][1] == "0":
            print("0 win")
        elif field[0][2] == "0" and field[1][2] == "0" and field[2][2] == "0":
            print("0 win")
        elif field[0][0] == "0" and field[1][1] == "0" and field[2][2] == "0":
            print("0 win")
        elif field[0][2] == "0" and field[1][1] == "0" and field[2][0] == "0":
            print("0 win")
        else:
            print("draw")


data = """x - x
0 - 0
x - -"""

field = [line.split() for line in data.split('\n')]
tic_tac_toe(field)
