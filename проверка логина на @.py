dic = {}
n = int(input())
for i in range(n):
    e = input().lower()
    s = ''.join(sorted(e))
    dic[s] = dic.get(s, set())
    dic[s].add(e)
new_words = [' '.join(sorted(i)) for i in dic.values() if len(i) > 1]
print('\n'.join(sorted(new_words)))
