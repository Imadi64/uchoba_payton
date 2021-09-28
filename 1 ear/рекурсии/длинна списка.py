def bracket_check(test_string):
    a = 0
    for i in test_string:
        if test_string == None:
            print("YES")
            break
        if i == "(":
            a += 1
        if i == ")":
            a -= 1
        if a < 0:
            break

    if a != 0:
        print("NO")

    else:
        print("YES")


bracket_check("())(()")
