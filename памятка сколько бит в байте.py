angl_ima = int(input())
nemetsk_ima = int(input())
iaziki = set()
familii = set()
for i in range(angl_ima + nemetsk_ima):
    familia = input()
    if familia in iaziki:
        familii.add(familia)
    else:
        iaziki.add(familia)
difference = iaziki - familii
if not difference:
    print('NO')
else:
    print(len(difference))
