import itertools
al = "НАСТЯ"
ar = itertools.product(al, repeat=6) 
a = []
for i in ar:
    a.append(list(i))
count = 0
for e in a:
    if e.count("А") <= 1 and e.count("Я") <= 1:
        count += 1
print(count)