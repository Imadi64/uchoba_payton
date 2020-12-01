import re
def listinput(mlist):
    i = int(input())
    for с in range(i):
        w = str(input())
        mlist.append(w)
    print(mlist)
    mlist = str(mlist)
    s = mlist.find('кот')
    print(s)
if __name__ == '__main__':
    mlist = []
    listinput(mlist)
