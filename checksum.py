s1 = list(map(int,list(input())))
s2 = list(map(int,list(input())))
n = len(s1)
res = [0 for i in range(n)]
c = 0

for i in range(n - 1, -1, -1):
    add = s1[i] + s2[i] + c 
    res[i] = add % 2 
    c = add // 2 
    
if c == 1:
    for i in range(n - 1, -1, -1):
        add = res[i] + c 
        res[i] = add % 2 
        c = add // 2 
        if c == 0:
            break
        
for i in res:
    print(int(not i), end = ' ')
    
