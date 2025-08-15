s = input()
v = c = ''
for ch in s:
    if ch.isalpha():
        ch = ch.lower()
        if ch in 'aiueo' and not v:
            v = ch
        elif ch not in 'aiueo' and not c:
            c = ch
    if v and c:
        break
print(v)
print(c)
